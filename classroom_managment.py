classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def helper(name):
    count=0
    for i in classroom:
        if(i['name']==name):
            return count
        count+=1
    return -1 
    
def add_student(name, email=None):
   if(email==None):
      nameLower=name.lower()
      email=f'<{nameLower}>@example.com'
      newStudent={'name':name,'email':email,'grades':[]}
   else:
      newStudent={'name':name,'email':email,'grades':[]}
   classroom.append(newStudent)
    


def delete_student(name):
    if(helper(name)!=-1):
      index=helper(name)
      del classroom[index]
    


def set_email(name, email):
    if(helper(name)!=-1):
        index=helper(name)
        classroom[index]['email']=email
    


def add_grade(name, profession, grade):
     if(helper(name)!=-1):
        index=helper(name)
        classroom[index]['grades'].append((profession,grade))
    


def avg_grade(name, profession):
    if(helper(name)!=-1):
        index=helper(name)
        sumGrade=0
        countGrade=0
        for i in classroom[index]['grades']:
            if(i[0]==profession):
              countGrade+=1
              sumGrade+=i[1]
        return sumGrade/countGrade
    


def get_professions(name):
     if(helper(name)!=-1):
        index=helper(name)
        l=[]
        for i in classroom[index]['grades']:
            if(l.__contains__(i[0])==False):
              l.append(i[0])
        return l
    pass
