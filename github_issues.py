import requests
import json
import getpass

class Github():
    def __init__(self, user, repo):
        try:
            with open('oauth.txt') as f:
                self.oauth_token = f.readline()
        except IOError:
            print('You do not seem to have oauth.txt with an oauth token.')
            print('Now requesting username and password to generate one.')
            self.create_authorization()
        self.user = user
        self.repo = repo
    
    def create_authorization(self):
        '''
        Create authorization as outlined at the link below
        http://developer.github.com/v3/oauth/#create-a-new-authorization
        '''
        username = raw_input('Username: ')
        password = getpass.getpass()
        payload = json.dumps({'scopes':['repo'], 'note':'google code migration'})
        request = requests.post('https://api.github.com/authorizations', 
                                auth=(username,password),
                                data=payload)
        self.oauth_token = request.json['token']
        f = open('oauth.txt','w')
        f.write(self.oauth_token)
        f.close();
        
    def create_issue(self, json):
        '''
        @return: http status code
        http://developer.github.com/v3/issues/
           'Create an issue'
        '''
        request = requests.post('https://api.github.com/repos/' +
                                self.user + '/' +
                                self.repo + '/' +
                                'issues', 
                                auth=(self.oauth_token,''),
                                data=json)
        return request.status_code

    def get_issue(self, number):
        '''
        @return: json (for issue number)
        http://developer.github.com/v3/issues/
           'Get a single issue'
        '''
        request = requests.get('https://api.github.com/repos/' +
                                self.user + '/' +
                                self.repo + '/' +
                                'issues/' +
                                str(number),
                                auth=(self.oauth_token,''))
        return request.json

    def get_issues(self):
        '''
        @return: json (issues)
        Return json data of all issues for self.user/self.repo
        http://developer.github.com/v3/issues/
           'List issues for a repository'
        '''
        request = requests.get('https://api.github.com/repos/' +
                                self.user + '/' +
                                self.repo + '/' +
                                'issues', 
                                auth=(self.oauth_token,''))
        return request.json

    def get_milestones(self):
        '''
        @return: json (milestones)
        http://developer.github.com/v3/issues/milestones/
           'List milestones for a repository'
        '''
        request = requests.get('https://api.github.com/repos/' +
                                self.user + '/' +
                                self.repo + '/' +
                                'milestones', 
                                auth=(self.oauth_token,''))
        return request.json
        
    def create_milestone(self, json):
        '''
        @return: http status code
        http://developer.github.com/v3/issues/milestones/
           'Create a milestone'
        '''
        request = requests.post('https://api.github.com/repos/' +
                                self.user + '/' +
                                self.repo + '/' +
                                'milestones', 
                                auth=(self.oauth_token,''),
                                data=json)
        return request.status_code

    def get_labels(self):
        '''
        @return: json (labels)
        http://developer.github.com/v3/issues/labels/
           'List all labels for a repository'
        '''
        request = requests.get('https://api.github.com/repos/' +
                                self.user + '/' +
                                self.repo + '/' +
                                'labels', 
                                auth=(self.oauth_token,''))
        return request.json
        
    def create_label(self, json):
        '''
        @return: http status code
        http://developer.github.com/v3/issues/labels/
           'Create a label'
        '''
        request = requests.post('https://api.github.com/repos/' +
                                self.user + '/' +
                                self.repo + '/' +
                                'labels', 
                                auth=(self.oauth_token,''),
                                data=json)
        print request.text
        return request.status_code
        


if __name__ == '__main__':
    pass