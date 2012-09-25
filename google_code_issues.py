import json
import requests

def get_google_code_issues(project_name):
    '''
    returns json data of google code issues
    '''
    request = requests.get('https://code.google.com/feeds/issues/p/' +
                           project_name +
                           '/issues/full?alt=json')
    json_data = json.loads(request.content)
    return json_data
    
def get_statuses(self):
    pass

def get_labels(self):
    pass
    
def get_milestones(self):
    pass
    
def get_priorities(self):
    pass

def get_types(self):
    pass
    
if __name__ == '__main__':
    pass
    