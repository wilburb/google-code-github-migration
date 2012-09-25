import google_code_issues

if __name__ == '__main__':
    json_data = google_code_issues.get_google_code_issues('reason-cms')
    for entry in json_data['feed']['entry']:
        github_entry[''] = entry['title']
        break # for now to create just one github issue
        

    testing = Github('wilburb','issue_migration_test')
    # payload = json.dumps({'title':'test title3', 'body': 'body text2',
    #                       'assignee':'wilburb'})
    payload = json.dumps({'name':'testlabel', 'color':'000000'})
    print testing.create_label(payload)