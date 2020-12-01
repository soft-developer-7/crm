from django.db import models


# Create your models here.

class User_db (models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(default='user',max_length=100)
    countrycode = models.CharField(max_length=10,null=True)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='profile/', default='profile/def.png',null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s %s" % (self.name)


class Posts(models.Model):
    title = models.CharField(max_length=300)
    
    meta = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    keywords = models.CharField(max_length=300)

    post = models.CharField(max_length=3000)

    banner_photo = models.ImageField(upload_to='post/', default='post/def.jpg',null=True,blank=True)
    body_photo = models.ImageField(upload_to='post/',null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User_db, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



class Pages(models.Model):
    title = models.CharField(max_length=300)
    
    meta = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    keywords = models.CharField(max_length=300)

    post = models.CharField(max_length=3000)

    body_photo = models.ImageField(upload_to='page/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Banners(models.Model):

    title = models.CharField(max_length=300)
    desc = models.CharField(max_length=500,null=True)
    alt = models.CharField(max_length=100,default='banner image')
    category = models.CharField(max_length=100,default='uncategorized')
    photo = models.ImageField(upload_to='banner/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class super_plan_forms_multiple_inputs(models.Model):                   # Multiple input fields
    form_id = models.CharField(max_length=10,null=True)
    user = models.ForeignKey(User_db, on_delete=models.CASCADE)
    f_1 = models.CharField(max_length=10000,null=True)
    f_2 = models.CharField(max_length=10000,null=True)
    f_3 = models.CharField(max_length=10000,null=True)
    f_4 = models.CharField(max_length=10000,null=True)
    f_5 = models.CharField(max_length=10000,null=True)
    f_6 = models.CharField(max_length=10000,null=True)
    f_7 = models.CharField(max_length=10000,null=True)
    f_8 = models.CharField(max_length=10000,null=True)
    f_9 = models.CharField(max_length=10000,null=True)
    f_10 = models.CharField(max_length=10000,null=True)
    f_11 = models.CharField(max_length=10000,null=True)
    f_12 = models.CharField(max_length=10000,null=True)
    f_13 = models.CharField(max_length=10000,null=True)
    f_14 = models.CharField(max_length=10000,null=True)
    f_15 = models.CharField(max_length=10000,null=True)
    f_16 = models.CharField(max_length=10000,null=True)
    f_17 = models.CharField(max_length=10000,null=True)
    f_18 = models.CharField(max_length=10000,null=True)
    f_19 = models.CharField(max_length=10000,null=True)
    f_20 = models.CharField(max_length=10000,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id




class super_plan_forms_multiple_images(models.Model):                           # Multiple Image
    form_id = models.CharField(max_length=10,null=True)
    user = models.ForeignKey(User_db, on_delete=models.CASCADE)
    i_1 = models.ImageField(upload_to='form_images/',null=True,blank=True)
    i_2 = models.ImageField(upload_to='form_images/',null=True,blank=True)
    i_3 = models.ImageField(upload_to='form_images/',null=True,blank=True)
    i_4 = models.ImageField(upload_to='form_images/',null=True,blank=True)
    i_5 = models.ImageField(upload_to='form_images/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id




class super_plan_forms_multiple_files(models.Model):                            # Multiple Files
    form_id = models.CharField(max_length=10,null=True)
    user = models.ForeignKey(User_db, on_delete=models.CASCADE)
    fi_1 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_2 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_3 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_4 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_5 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_6 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_7 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_8 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_9 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    fi_10 = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id











class super_plan_forms(models.Model):


    # Form- 0 ----------------------------------------------------------------------------------------- 11 -------------
    theme = models.CharField(max_length=500,null=True)
    currency = models.CharField(max_length=50,null=True)
    denomination  = models.CharField(max_length=50,null=True)
    pack = models.CharField(max_length=100,null=True)

    # Form-1------------------------------------------------------------------------------------- 1 --------------------
    user = models.ForeignKey(User_db, on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=1000,null=True)
    company_website_link = models.CharField(max_length=1000,null=True)
    owner_name = models.CharField(max_length=500,null=True)
    countrycode = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=13,null=True)
    email_id = models.CharField(max_length=500,null=True)
    gst_number = models.CharField(max_length=100,null=True)
    gst_name = models.CharField(max_length=500,null=True)

    # Form-2----------------------------------------------------------------------------------------2 -----------------
    about_the_company = models.CharField(max_length=7000,null=True)
    company_logo = models.ImageField(upload_to='superplan-files/',null=True,blank=True)
    company_founded = models.CharField(max_length=100,null=True)
    industry_type = models.CharField(max_length=1000,null=True)

    # Form-3------------------------------------------------------------------------------------------3 ---------------
    challenges_faced = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='challenges_faced',on_delete=models.SET_NULL, null=True)
    solutions_provided = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='solutions_provided',on_delete=models.SET_NULL, null=True)

    # Form-4--------------------------------------------------------------------------------------------4 -------------
    products_and_services = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='products_and_services',on_delete=models.SET_NULL, null=True)
    products_and_services_file = models.ForeignKey(super_plan_forms_multiple_images,related_name='products_and_services_file',on_delete=models.SET_NULL, null=True)
    top_clients = models.CharField(max_length=2000,null=True)
    top_clients_file = models.FileField(upload_to='superplan-files/',null=True,blank=True)
    milestones = models.CharField(max_length=1000,null=True)
    locations_served = models.CharField(max_length=1000,null=True)
    swot_s = models.CharField(max_length=1000,null=True)
    swot_w = models.CharField(max_length=1000,null=True)
    swot_o = models.CharField(max_length=1000,null=True)
    swot_t = models.CharField(max_length=1000,null=True)

    # Form-5---------------------------------------------------------------------------------------------5 ------------
    management_team_name = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='management_team_name',on_delete=models.SET_NULL, null=True)
    management_team_file = models.ForeignKey(super_plan_forms_multiple_images,related_name='management_team_file',on_delete=models.SET_NULL, null=True)
    management_team_contact = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='management_team_contact',on_delete=models.SET_NULL, null=True)
    management_team_designation = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='management_team_designation',on_delete=models.SET_NULL, null=True)
    

    # For-6-----------------------------------------------------------------------------------------------6 ----------
    marketing_strategies = models.CharField(max_length=8000,null=True)
    growth_strategy = models.CharField(max_length=8000,null=True)

    # Form-7-----------------------------------------------------------------------------------------------7 ----------
    industry_analysis = models.CharField(max_length=8000,null=True)
    competitor_analysis = models.CharField(max_length=8000,null=True)
    usp = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='usp',on_delete=models.SET_NULL, null=True)



    # Form-8-------------------------------------------------------------------------------------------------8 ---------
    revenue_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_income_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_income_growth_or_amount',on_delete=models.SET_NULL, null=True)

    total_revenue_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_revenue_amount',on_delete=models.SET_NULL, null=True)

    operating_expenses_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='operating_expenses_growth_or_amount',on_delete=models.SET_NULL, null=True)

    employee_cost = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='employee_cost',on_delete=models.SET_NULL, null=True)

    general_and_administration_cost = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='general_and_administration_cost',on_delete=models.SET_NULL, null=True)

    selling_and_marketing_cost = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='selling_and_marketing_cost',on_delete=models.SET_NULL, null=True)

    other_expenses_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_expenses_growth_or_amount',on_delete=models.SET_NULL, null=True)

    ebitda = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='ebitda',on_delete=models.SET_NULL, null=True)

    depreciation_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='depreciation_or_amount',on_delete=models.SET_NULL, null=True)

    interest_expense_interest_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='interest_expense_interest_or_amount',on_delete=models.SET_NULL, null=True)

    ebt = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='ebt',on_delete=models.SET_NULL, null=True)

    tax_expense_tax_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='tax_expense_tax_or_amount',on_delete=models.SET_NULL, null=True)

    pat = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='pat',on_delete=models.SET_NULL, null=True)




    # Form -9 ----------------------------------------------------------------------------------------------9 ----------
    share_capital = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='share_capital',on_delete=models.SET_NULL, null=True)

    reserves_and_surplus = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='reserves_and_surplus',on_delete=models.SET_NULL, null=True)

    fund_requirement = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='fund_requirement',on_delete=models.SET_NULL, null=True)

    total_shareholder_funds = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_shareholder_funds',on_delete=models.SET_NULL, null=True)

    secured_loans = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='secured_loans',on_delete=models.SET_NULL, null=True)

    unsecured_loans = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='unsecured_loans',on_delete=models.SET_NULL, null=True)

    long_term_provisions_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_provisions_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_non_current_liabilities_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_non_current_liabilities_growth_or_amount',on_delete=models.SET_NULL, null=True)

    total_non_current_liabilities = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_non_current_liabilities',on_delete=models.SET_NULL, null=True)

    short_term_borrowings_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_borrowings_growth_or_amount',on_delete=models.SET_NULL, null=True)

    short_term_provisions_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_provisions_growth_or_amount',on_delete=models.SET_NULL, null=True)

    sundry_creditors_no_of_days_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='sundry_creditors_no_of_days_or_amount',on_delete=models.SET_NULL, null=True)

    other_current_liabilities_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_current_liabilities_growth_or_amount',on_delete=models.SET_NULL, null=True)

    total_current_liabilities = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_current_liabilities',on_delete=models.SET_NULL, null=True)

    total_liabilities = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_liabilities',on_delete=models.SET_NULL, null=True)

    gross_fixed_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='gross_fixed_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    less_accumulated_depreciation_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='less_accumulated_depreciation_or_amount',on_delete=models.SET_NULL, null=True)

    net_fixed_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='net_fixed_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    intangible_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='intangible_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    long_term_loans_and_advances_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_loans_and_advances_growth_or_amount',on_delete=models.SET_NULL, null=True)

    long_term_investments_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_investments_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_non_current_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_non_current_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    total_non_current_assets = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_non_current_assets',on_delete=models.SET_NULL, null=True)

    cash = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='cash',on_delete=models.SET_NULL, null=True)

    sundry_debtors_no_of_days_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='sundry_debtors_no_of_days_or_amount',on_delete=models.SET_NULL, null=True)

    inventory_no_of_days_or_amount  = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='inventory_no_of_days_or_amount',on_delete=models.SET_NULL, null=True)

    short_term_investments_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_investments_growth_or_amount',on_delete=models.SET_NULL, null=True)

    short_term_loans_and_advances_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_loans_and_advances_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_current_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_current_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    total_current_assets = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_current_assets',on_delete=models.SET_NULL, null=True)

    total_assets = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_assets',on_delete=models.SET_NULL, null=True)

    # Form- 10 ----------------------------------------------------------------------------------------- 10 -------------

    company_owned_land_and_building = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='company_owned_land_and_building',on_delete=models.SET_NULL, null=True)

    other_fixed_assets  = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_fixed_assets',on_delete=models.SET_NULL, null=True)

    depreciation_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='depreciation_growth_or_amount',on_delete=models.SET_NULL, null=True)

    total_capex_expense = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='total_capex_expense',on_delete=models.SET_NULL, null=True)








    current_fillup_position = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.user.name







#-----------------------------------------------------------------------------------------------------------------

