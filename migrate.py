import requests
import json
from random import randrange

import github_issues

def add_label(github, color_list, label_name):
    color = None
    while color == None:
        temp_color = "".join([hex(randrange(0, 255))[2:] for i in range(3)])
        if temp_color not in color_list:
            color_list.append(temp_color)
            color = temp_color
    payload = json.dumps({'name':label_name, 'color':color})
    github.create_label(payload)

if __name__ == '__main__':
    github = github_issues.Github('wilburb','issue_migration_test')
    
    # get current github labels
    github_labels = github.get_labels()
    label_colors = []
    label_names = []
    for label in github_labels:
        label_colors.append(label['color'])
        label_names.append(label['name'])
    
    # get current github milestones
    github_milestones = github.get_milestones()
    milestones = []
    for milestone in github_milestones:
        milestones.append(milestone['title'])
    
    all_issues = requests.get('https://code.google.com/feeds/issues/p/' +
                              'reason-cms/issues/full?alt=json&max-results=10000').json
    new_issues = []
    break_time = 0
    for entry in all_issues['feed']['entry']:
        new_issue = {}
        new_issues.append(new_issue)
        #print(google_code_issues.get_url(entry['id']['$t']))
        new_issue['id'] = entry['issues$id']['$t']
        new_issue['title'] = entry['title']['$t']
        if entry['issues$status']['$t'] not in label_names:
            add_label(github, label_colors, entry['issues$status']['$t'])
            label_names.append(entry['issues$status']['$t'])
        new_issue['labels'] = [entry['issues$status']['$t']]
        new_issue['state'] = entry['issues$state']['$t']
        if entry['issues$stars']['$t'] not in label_names:
            add_label(github, label_colors, entry['issues$stars']['$t'])
            label_names.append(entry['issues$stars']['$t'])
        new_issue['labels'].append(str(entry['issues$stars']['$t'])+'_stars')
        new_issue['description'] = entry['content']['$t']
        try:
            new_issue['closed_date'] = entry['issues$closedDate']['$t']
        except KeyError:
            new_issue['closed_date'] = ''
        for label in entry['issues$label']:
            if (label['$t'][:9] == 'Milestone'):
                if label['$t'] not in milestones:
                    payload = json.dumps({'title':label['$t']})
                    github.create_milestone(payload)
                    milestones.append(label['$t'])
                new_issue['milestone'] = label['$t'][10:]
            else:
                if label['$t'] not in label_names:
                    add_label(github, label_colors, label['$t'])
                    label_names.append(label['$t'])
                new_issue['labels'].append(label['$t'])
        comments = requests.get('https://code.google.com/feeds/issues/p/' +
                                'reason-cms/issues/' + str(new_issue['id']) +
                                '/comments/full/?alt=json&max-results=1000').json
        new_issue['comments'] = []
        try:
            for comment in comments['feed']['entry']:
                new_issue['comments'].append(comment['content']['$t'])
        except KeyError:
            pass # no comments to add
        #break_time += 1
        #if break_time > 5:
        #    break
    
    # json_data = google_code_issues.get_google_code_issues('reason-cms')
    #     for entry in json_data['feed']['entry']:
    #         github_entry[''] = entry['title']
    #         break # for now to create just one github issue
    #         
    # 
    #     testing = Github('wilburb','issue_migration_test')
    #     # payload = json.dumps({'title':'test title3', 'body': 'body text2',
    #     #                       'assignee':'wilburb'})
    #     payload = json.dumps({'name':'testlabel', 'color':'000000'})
    #     print testing.create_label(payload)