import requests
import json

import github_issues

if __name__ == '__main__':
    all_issues = requests.get('https://code.google.com/feeds/issues/p/' +
                              'reason-cms/issues/full?max_results=10000;alt=json').json
    print all_issues
    new_issues = []
    for entry in all_issues['feed']['entry']:
        new_issue = {}
        new_issues.append(new_issue)
        #print(google_code_issues.get_url(entry['id']['$t']))
        new_issue['id'] = entry['issues$id']['$t']
        new_issue['title'] = entry['title']['$t']
        new_issue['labels'] = [entry['issues$status']['$t']]
        new_issue['state'] = entry['issues$state']['$t']
        new_issue['labels'].append(str(entry['issues$stars']['$t'])+'_stars')
        new_issue['description'] = entry['content']['$t']
        new_issue['closed_date'] = entry['issues$closedDate']['$t']
        for label in entry['issues$label']:
            if (label['$t'][:9] == 'Milestone'):
                new_issue['milestone'] = label['$t'][10:]
            else:
                new_issue['labels'].append(label['$t'])
        comments = requests.get('https://code.google.com/feeds/issues/p/' +
                                'reason-cms/issues/' + str(new_issue['id']) +
                                '/comments/full/?max_results=1000;alt=json').json
                                
        print comments
        break
    
    
    # u'link': [{u'href': u'http://code.google.com/feeds/issues/p/reason-cms/issues/12/comments/full', 
    #                u'type': u'application/atom+xml', u'rel': u'replies'}, 
    #               {u'href': u'http://code.google.com/p/reason-cms/issues/detail?id=12', 
    #                u'type': u'text/html', u'rel': u'alternate'}, 
    #               {u'href': u'http://code.google.com/feeds/issues/p/reason-cms/issues/full/12', 
    #                u'type': u'application/atom+xml', u'rel': u'self'}
    #              ]
    
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