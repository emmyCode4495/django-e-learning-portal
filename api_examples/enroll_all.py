import requests

username = 'learning'
password = 'emmy4495'

base_url = 'http://127.0.0.1:8000/api/v1/'

# retrieve all courses

r = requests.get(f'{base_url}courses/')
courses = r.json()

available_courses = ', '.join([course['title'] for course in courses])
print(f'Available Courses: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}courses/{course_id}/enroll/',
                                            auth=(username,password))
    if r.status_code == 200:
        # Successful request
        print(f'successfully enrolled in {course_title}')