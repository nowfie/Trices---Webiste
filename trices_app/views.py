from django.shortcuts import render

# Create your views here.

def list_of_services():
    services = {
        'Artificial Intelligence': {
            'icon': '<i class="fa-solid fa-microchip p-lg-4 p-3"></i>',
            'heading':'Powering Your Business Potential through Intelligence',
            'description': 'Harness the potential of Artificial Intelligence to transform data into insights, driving innovation and intelligent decision-making.',
            #'image':'ai.jpg'
        },
        'Data Science & Analytics': {
            'icon': '<i class="fa-solid fa-magnifying-glass-chart p-lg-4 p-3"></i>',
            'heading':'Empowering Decisions through Data Insights',
            'description': 'Unlock the power of Data Science and Analytics services, turning information into actionable insights to fuel strategic growth.',
            #'image':'ds.jpg'
        },
        'Web Application': {
            'icon': '<i class="fa-solid fa-code p-lg-4 p-3"></i>',
            'heading':'Enriching Experiences, One App at a Time',
            'description': 'Dynamic and user-centric web applications that seamlessly blend functionality and design, delivering an exceptional online experience.',
            #'image':'web.jpg'
        },
        'Mobile Application': {
            'icon': '<i class="fa fa-mobile p-lg-4 p-3" aria-hidden="true"></i>',
            'heading':'Enriching Experiences, One App at a Time',
            'description': 'Elevate your business with our Mobile App Development expertise, creating intuitive and feature-rich applications for a mobile-first world.',
            #'image':'mobile.jpg'
        },
        'Social Media Marketing': {
            'icon': '<i class="fa-solid fa-chart-simple p-lg-4 p-3"></i>',
            'heading':'Maximizing Online Potential through SEO Mastery',
            'description': 'Maximize your online presence and engagement through our Digital Marketing strategies,and connecting your brand with the right audience.',
            #'image':'marketing.jpg'
        },
        'Search Engine Optimization': {
            'icon': '<i class="fas fa-business-time p-lg-4 p-3"></i>',
            'heading':'Navigating the Future of Social Media Marketing',
            'description': 'Optimizing a website service for SEO enhances online visibility and attracts more relevant users through strategic content and structural improvements',
            #'image':'ai.jpg'
        }
    }
    return services
def team_members():
    team = {
        'Mohammed Nowfal': {
            'role':'Team Leader',
            'image': 'person1.png'              
        },
        'Venketakrishnan': {
            'role':'Data Scientist',
            'image': 'person1.png'              
        },
        'Wasim hussain': {
            'role':'Marketing Lead',
            'image': 'person1.png'              
        }
    }
    return team
    

def home(request):
    services = list_of_services()
    context = {'services': services}
    return render(request,'trices_app/base/home.html',context)

def about(request):
    team_function = team_members()
    context = {'team_function':team_function}
    return render(request,'trices_app/base/about.html',context)

def services(request):
    services = list_of_services()
    context = {'services': services}
    return render(request,'trices_app/base/services.html',context)

def ser_ind(request,name):
    services_list=list_of_services()
    content=services_list[name]
    context = {'content':content,'name':name}
    return render(request,'trices_app/base/services_ind.html',context)

def contact(request):
    return render(request,'trices_app/base/contact.html')
    