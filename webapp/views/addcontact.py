from django.views import View
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from webapp.models import Contact

class AddContacts(View):
    def get(self, request):
        return render(request, 'add.htm')
    
    def post(self, request):
        contact_type = request.POST.get('contact_type')
        full_name = request.POST.get('full_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        title = request.POST.get('title')
        dept = request.POST.get('dept')
        university = request.POST.get('university')
        degree = request.POST.get('degree')
        passing_year = request.POST.get('passing_year')
        college = request.POST.get('college')
        linkedin_url = request.POST.get('linkedin_url')
        facebook_url = request.POST.get('facebook_url')
        skype_id = request.POST.get('skype_id')
        industry = request.POST.get('industry')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        key_skills = request.POST.get('key_skills')
        total_exp = request.POST.get('total_exp')
        years_in_business = request.POST.get('years_in_business')
        cin_no = request.POST.get('cin_no')
        turnover = request.POST.get('turnover')
        incorporation_date = request.POST.get('incorporation_date')
        employees = request.POST.get('employees')
        ctc = request.POST.get('ctc')
        
        
        cont_instance = Contact(contact_type=contact_type, full_name=full_name, first_name=first_name, middle_name=middle_name, last_name=last_name, company=company, designation=designation, email=email, phone=phone, location=location, gender=gender, title=title, dept=dept, university=university, degree=degree, passing_year=passing_year, college=college, linkedin_url=linkedin_url, facebook_url=facebook_url, skype_id=skype_id, industry=industry, country=country, state=state, zip_code=zip_code, key_skills=key_skills, total_exp=total_exp, years_in_business=years_in_business, cin_no=cin_no, turnover=turnover, incorporation_date=incorporation_date, employees=employees, ctc=ctc)
        cont_instance.save()
        return(render(request, 'add.htm'))

    
