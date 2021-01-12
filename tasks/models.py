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
    i_6 = models.ImageField(upload_to='form_images/',null=True,blank=True)
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


    # Form- 1 ----------------------------------------------------------------------------------------- 1 -------------
    theme = models.CharField(max_length=500,null=True)
    currency = models.CharField(max_length=50,null=True)
    denomination  = models.CharField(max_length=50,null=True)
    pack = models.CharField(max_length=100,null=True)

    # Form-2------------------------------------------------------------------------------------- 2 --------------------
    user = models.ForeignKey(User_db, on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=1000,null=True)
    company_website_link = models.CharField(max_length=1000,null=True)
    owner_name = models.CharField(max_length=500,null=True)
    countrycode = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=13,null=True)
    email_id = models.CharField(max_length=500,null=True)
    gst_number = models.CharField(max_length=100,null=True)
    gst_name = models.CharField(max_length=500,null=True)

    # Form-3----------------------------------------------------------------------------------------3 -----------------
    about_the_company = models.CharField(max_length=7000,null=True)
    company_logo = models.ImageField(upload_to='superplan-files/',null=True,blank=True)
    company_founded = models.CharField(max_length=100,null=True)
    industry_type = models.IntegerField(null=True)

    # Form-4------------------------------------------------------------------------------------------4 ---------------
    challenges_faced = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='challenges_faced',on_delete=models.SET_NULL, null=True)
    solutions_provided = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='solutions_provided',on_delete=models.SET_NULL, null=True)

    # Form-5--------------------------------------------------------------------------------------------5 -------------
    products_and_services = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='products_and_services',on_delete=models.SET_NULL, null=True)
    products_and_services_file = models.ForeignKey(super_plan_forms_multiple_images,related_name='products_and_services_file',on_delete=models.SET_NULL, null=True)
    
    top_clients = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='top_clients',on_delete=models.SET_NULL, null=True)
    top_clients_file = models.ForeignKey(super_plan_forms_multiple_images,related_name='top_clients_file',on_delete=models.SET_NULL, null=True)
    
    milestones_time = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='milestones_time',on_delete=models.SET_NULL, null=True)
    milestones_achievement = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='milestones_achievement',on_delete=models.SET_NULL, null=True)
    
    locations_served = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='locations_served',on_delete=models.SET_NULL, null=True)
    
    swot_s = models.CharField(max_length=1000,null=True)
    swot_w = models.CharField(max_length=1000,null=True)
    swot_o = models.CharField(max_length=1000,null=True)
    swot_t = models.CharField(max_length=1000,null=True)

    # Form-6---------------------------------------------------------------------------------------------6 ------------
    management_team_name = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='management_team_name',on_delete=models.SET_NULL, null=True)
    management_team_file = models.ForeignKey(super_plan_forms_multiple_images,related_name='management_team_file',on_delete=models.SET_NULL, null=True)
    management_team_contact = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='management_team_contact',on_delete=models.SET_NULL, null=True)
    management_team_designation = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='management_team_designation',on_delete=models.SET_NULL, null=True)
    

    # For-7-----------------------------------------------------------------------------------------------7 ----------
    marketing_strategies_offline = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='marketing_strategies_offline',on_delete=models.SET_NULL, null=True)
    marketing_strategies_online = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='marketing_strategies_online',on_delete=models.SET_NULL, null=True)


    # For-8-----------------------------------------------------------------------------------------------8 ----------
    growth_strategy = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='growth_strategy',on_delete=models.SET_NULL, null=True)

    # Form-9-----------------------------------------------------------------------------------------------9 ----------
    industry_analysis_glob = models.CharField(max_length=8000,null=True)
    industry_analysis_glob_img = models.ImageField(upload_to='superplan-files/',null=True,blank=True)

    industry_analysis_india = models.CharField(max_length=8000,null=True)
    industry_analysis_india_img = models.ImageField(upload_to='superplan-files/',null=True,blank=True)
    
    competitor_analysis_n = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='competitor_analysis_n',on_delete=models.SET_NULL, null=True)
    competitor_analysis_p = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='competitor_analysis_p',on_delete=models.SET_NULL, null=True)
    competitor_analysis_v1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='competitor_analysis_v1',on_delete=models.SET_NULL, null=True)
    competitor_analysis_v2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='competitor_analysis_v2',on_delete=models.SET_NULL, null=True)
    competitor_analysis_v3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='competitor_analysis_v3',on_delete=models.SET_NULL, null=True)
    competitor_analysis_v4 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='competitor_analysis_v4',on_delete=models.SET_NULL, null=True)
    competitor_analysis_v5 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='competitor_analysis_v5',on_delete=models.SET_NULL, null=True)
    industry_growth_drivers = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='industry_growth_drivers',on_delete=models.SET_NULL, null=True)
    usp = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='usp',on_delete=models.SET_NULL, null=True)

    # Form-9.1----------------------------------------------------------------------------------------- 9.1------------
    historical_xl = models.ImageField(upload_to='superplan-files/',null=True,blank=True)


    # Form-10-------------------------------------------------------------------------------------------------10 ---------
    profit_and_loss_years = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='profit_and_loss_years',on_delete=models.SET_NULL, null=True)

    revenue_growth_or_amount_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_1',on_delete=models.SET_NULL, null=True)
    revenue_growth_1_or = models.CharField(max_length=100,null=True)

    revenue_growth_or_amount_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_2',on_delete=models.SET_NULL, null=True)
    revenue_growth_2_or = models.CharField(max_length=100,null=True)

    revenue_growth_or_amount_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_3',on_delete=models.SET_NULL, null=True)
    revenue_growth_3_or = models.CharField(max_length=100,null=True)

    revenue_growth_or_amount_4 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_4',on_delete=models.SET_NULL, null=True)
    revenue_growth_4_or = models.CharField(max_length=100,null=True)

    other_income_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_income_growth_or_amount', on_delete=models.SET_NULL, null=True)
    other_income_growth_or = models.CharField(max_length=100,null=True)


    realised_foreign_exchange_gain_or_loss = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='realised_foreign_exchange_gain_or_loss', on_delete=models.SET_NULL, null=True)
    realised_foreign_exchange_gain_or = models.CharField(max_length=100,null=True)


    direct_material_units = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_material_units', on_delete=models.SET_NULL, null=True)

    direct_material_average_cost_per_unit =models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_material_average_cost_per_unit', on_delete=models.SET_NULL, null=True) 

    direct_labour_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_labour_no_of_employees', on_delete=models.SET_NULL, null=True)

    direct_labour_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_labour_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    other_direct_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_direct_expenses_1', on_delete=models.SET_NULL, null=True)

    other_direct_expenses_2 =models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_direct_expenses_2', on_delete=models.SET_NULL, null=True)

    other_direct_expenses_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_direct_expenses_3', on_delete=models.SET_NULL, null=True)


    administration_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='administration_no_of_employees', on_delete=models.SET_NULL, null=True)

    administration_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='administration_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    selling_and_distribution_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='selling_and_distribution_no_of_employees', on_delete=models.SET_NULL, null=True)

    selling_and_distribution_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='selling_and_distribution_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    marketing_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='marketing_no_of_employees', on_delete=models.SET_NULL, null=True)

    marketing_average_cost_per_employee =models.ForeignKey(super_plan_forms_multiple_inputs,related_name='marketing_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    research_and_development_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='research_and_development_no_of_employees', on_delete=models.SET_NULL, null=True)

    research_and_development_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='research_and_development_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    other_employees_1  = models.CharField(max_length=100,null=True)
    other_employees_1_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_employees_1_no_of_employees', on_delete=models.SET_NULL, null=True)

    other_employees_1_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_employees_1_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    other_employees_2 = models.CharField(max_length=100,null=True)

    other_employees_2_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_employees_2_no_of_employees', on_delete=models.SET_NULL, null=True)

    other_employees_2_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_employees_2_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    other_employees_3 = models.CharField(max_length=100,null=True)

    other_employees_3_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_employees_3_no_of_employees', on_delete=models.SET_NULL, null=True)

    other_employees_3_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_employees_3_average_cost_per_employee', on_delete=models.SET_NULL, null=True)

    rent = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='rent', on_delete=models.SET_NULL, null=True)

    telephone_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='telephone_expenses', on_delete=models.SET_NULL, null=True)

    electricity = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='electricity', on_delete=models.SET_NULL, null=True)

    printing_and_stationery = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='printing_and_stationery', on_delete=models.SET_NULL, null=True)

    audit_fees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='audit_fees', on_delete=models.SET_NULL, null=True)


    other_administration_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_administration_expenses_1', on_delete=models.SET_NULL, null=True)

    other_administration_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_administration_expenses_2', on_delete=models.SET_NULL, null=True)

    other_administration_expenses_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_administration_expenses_3', on_delete=models.SET_NULL, null=True)

    digital_marketing_cost = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='digital_marketing_cost', on_delete=models.SET_NULL, null=True)

    sales_commissions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='sales_commissions', on_delete=models.SET_NULL, null=True)

    travelling_expenses  = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='travelling_expenses', on_delete=models.SET_NULL, null=True)

    advertisement = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='advertisement', on_delete=models.SET_NULL, null=True)

    logistics_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='logistics_expenses', on_delete=models.SET_NULL, null=True)


    other_selling_and_marketing_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_selling_and_marketing_expenses_1', on_delete=models.SET_NULL, null=True)

    other_selling_and_marketing_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_selling_and_marketing_expenses_2', on_delete=models.SET_NULL, null=True)

    other_selling_and_marketing_expenses_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_selling_and_marketing_expenses_3', on_delete=models.SET_NULL, null=True)

    other_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_expenses_1', on_delete=models.SET_NULL, null=True)

    other_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_expenses_2', on_delete=models.SET_NULL, null=True)


    income_tax_rate = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='income_tax_rate', on_delete=models.SET_NULL, null=True)




    # Form -11 ----------------------------------------------------------------------------------------------9 ----------
    
    balance_sheet_years = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='balance_sheet_years',on_delete=models.SET_NULL, null=True)

    share_capital = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='share_capital',on_delete=models.SET_NULL, null=True)

    reserves_and_surplus = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='reserves_and_surplus',on_delete=models.SET_NULL, null=True)

    equity_funds_raised = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='equity_funds_raised',on_delete=models.SET_NULL, null=True)



    secured_loans_from_banks = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='secured_loans_from_banks',on_delete=models.SET_NULL, null=True)

    secured_loans_term_loans = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='secured_loans_term_loans',on_delete=models.SET_NULL, null=True)

    secured_loans_other_loans = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='secured_loans_other_loans',on_delete=models.SET_NULL, null=True)

    secured_loans_finance_lease_obligation = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='secured_loans_finance_lease_obligation',on_delete=models.SET_NULL, null=True)

    unsecured_loans = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='unsecured_loans',on_delete=models.SET_NULL, null=True)

    average_interest_rate_debt = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='average_interest_rate_debt',on_delete=models.SET_NULL, null=True)

    deferred_tax_liabilities  = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='deferred_tax_liabilities',on_delete=models.SET_NULL, null=True)

    long_term_provisions_growth_or = models.CharField(max_length=100,null=True)

    long_term_provisions_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_provisions_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_non_current_liabilities_growth_or = models.CharField(max_length=100,null=True)

    other_non_current_liabilities_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_non_current_liabilities_growth_or_amount',on_delete=models.SET_NULL, null=True)





    short_term_borrowings_growth_or = models.CharField(max_length=100,null=True)

    short_term_borrowings_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_borrowings_growth_or_amount',on_delete=models.SET_NULL, null=True)


    short_term_provisions_growth_or = models.CharField(max_length=100,null=True)

    short_term_provisions_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_provisions_growth_or_amount',on_delete=models.SET_NULL, null=True)


    sundry_creditors_no_of_days = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='sundry_creditors_no_of_days',on_delete=models.SET_NULL, null=True)

    other_current_liabilities_growth_or = models.CharField(max_length=100,null=True)

    other_current_liabilities_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_current_liabilities_growth_or_amount',on_delete=models.SET_NULL, null=True)





    intangible_assets_growth_or = models.CharField(max_length=100,null=True)

    intangible_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='intangible_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)


    long_term_loans_and_advances_growth_or = models.CharField(max_length=100,null=True)

    long_term_loans_and_advances_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_loans_and_advances_growth_or_amount',on_delete=models.SET_NULL, null=True)


    long_term_investments_growth_or = models.CharField(max_length=100,null=True)

    long_term_investments_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_investments_growth_or_amount',on_delete=models.SET_NULL, null=True)

    deferred_tax_assets_or = models.CharField(max_length=100,null=True)

    deferred_tax_assets = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='deferred_tax_assets',on_delete=models.SET_NULL, null=True)

    other_non_current_assets_growth_or = models.CharField(max_length=100,null=True)

    other_non_current_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_non_current_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)




    sundry_debtors_no_of_days = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='sundry_debtors_no_of_days',on_delete=models.SET_NULL, null=True)

    inventory_no_of_days = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='inventory_no_of_days',on_delete=models.SET_NULL, null=True)

    short_term_investments_growth_or = models.CharField(max_length=100,null=True)

    short_term_investments_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_investments_growth_or_amount',on_delete=models.SET_NULL, null=True)

    short_term_loans_and_advances_growth_or = models.CharField(max_length=100,null=True)

    short_term_loans_and_advances_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_loans_and_advances_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_current_assets_growth_or = models.CharField(max_length=100,null=True)

    other_current_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_current_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    working_capital = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='working_capital',on_delete=models.SET_NULL, null=True)



    # Form- 12 ----------------------------------------------------------------------------------------- 10 -------------

    capex_years = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_years',on_delete=models.SET_NULL, null=True)

    capex_opening_gross = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_opening_gross',on_delete=models.SET_NULL, null=True)
    

    capex_additions_or = models.CharField(max_length=100,null=True)
    capex_additions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_additions',on_delete=models.SET_NULL, null=True)

    capex_additions_intangible_or = models.CharField(max_length=100,null=True)
    capex_additions_intangible = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_additions_intangible',on_delete=models.SET_NULL, null=True)

    capex_deletions_or = models.CharField(max_length=100,null=True)
    capex_deletions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_deletions',on_delete=models.SET_NULL, null=True)

    capex_average_depreciation_rate = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_average_depreciation_rate',on_delete=models.SET_NULL, null=True)


    current_fillup_position = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.user.name







#-----------------------------------------------------------------------------------------------------------------

