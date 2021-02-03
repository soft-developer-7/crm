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




class super_plan_forms_multiple_inputs_xl(models.Model):                   # Multiple input fields
    form_id = models.CharField(max_length=10,null=True)
    f_2 = models.CharField(max_length=100,null=True)
    f_3 = models.CharField(max_length=100,null=True)
    f_1 = models.CharField(max_length=100,null=True)
    f_4 = models.CharField(max_length=100,null=True)
    f_5 = models.CharField(max_length=100,null=True)
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



class super_plan_form_xl_input(models.Model):
    form_id=form_id = models.CharField(max_length=10)

    capex_schedule_opening_gross   = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_opening_gross',on_delete=models.SET_NULL, null=True)

    capex_schedule_additions = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_additions',on_delete=models.SET_NULL, null=True)

    capex_schedule_additions_intangible = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_additions_intangible',on_delete=models.SET_NULL, null=True)

    capex_schedule_deletions = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_deletions',on_delete=models.SET_NULL, null=True)

    capex_schedule_closing_gross = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_closing_gross',on_delete=models.SET_NULL, null=True)

    capex_schedule_accumulated_depreciation = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_accumulated_depreciation',on_delete=models.SET_NULL, null=True)

    capex_schedule_net_value = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_net_value',on_delete=models.SET_NULL, null=True)

    capex_schedule_current_depreciation = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_current_depreciation',on_delete=models.SET_NULL, null=True)

    capex_schedule_average_depreciation_rate = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='capex_schedule_average_depreciation_rate',on_delete=models.SET_NULL, null=True)

    debt_schedule_secured_loans_from_banks = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_secured_loans_from_banks',on_delete=models.SET_NULL, null=True)

    debt_schedule_secured_loans_term_loans = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_secured_loans_term_loans',on_delete=models.SET_NULL, null=True)

    debt_schedule_secured_loans_othe_loans = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_secured_loans_othe_loans',on_delete=models.SET_NULL, null=True)

    debt_schedule_secured_loans_finance_lease_obligation = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_secured_loans_finance_lease_obligation',on_delete=models.SET_NULL, null=True)

    debt_schedule_secured_loans_total_secured_loans = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_secured_loans_total_secured_loans',on_delete=models.SET_NULL, null=True)

    debt_schedule_unsecured_loans = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_unsecured_loans',on_delete=models.SET_NULL, null=True)

    debt_schedule_total_unsecured_loan = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_total_unsecured_loan',on_delete=models.SET_NULL, null=True)

    debt_schedule_total_debt  = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_total_debt',on_delete=models.SET_NULL, null=True)

    debt_schedule_interest_expense  = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_interest_expense',on_delete=models.SET_NULL, null=True)

    debt_schedule_average_interest_rate = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='debt_schedule_average_interest_rate',on_delete=models.SET_NULL, null=True)

    income_statement_revenue_stream_1 = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_revenue_stream_1',on_delete=models.SET_NULL, null=True)

    income_statement_revenue_stream_2 = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_revenue_stream_2',on_delete=models.SET_NULL, null=True)

    income_statement_revenue_stream_3 = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_revenue_stream_3',on_delete=models.SET_NULL, null=True)

    income_statement_revenue_stream_4 = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_revenue_stream_4',on_delete=models.SET_NULL, null=True)

    income_statement_total_revenue_from_operations_services = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_total_revenue_from_operations_services',on_delete=models.SET_NULL, null=True)

    income_statement_product_development_expenses_operating_expenses_raw_material = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_product_development_expenses_operating_expenses_raw_material',on_delete=models.SET_NULL, null=True)

    income_statement_employee_cost = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_employee_cost',on_delete=models.SET_NULL, null=True)

    income_statement_general_and_administrative_expenses = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_general_and_administrative_expenses',on_delete=models.SET_NULL, null=True)

    income_statement_selling_and_marketing_expenses = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_selling_and_marketing_expenses',on_delete=models.SET_NULL, null=True)

    income_statement_other_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_other_expenses_1',on_delete=models.SET_NULL, null=True)

    income_statement_other_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_other_expenses_2',on_delete=models.SET_NULL, null=True)

    income_statement_total_operating_expenses = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_total_operating_expenses',on_delete=models.SET_NULL, null=True)

    income_statement_ebitda_operating_profit = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_ebitda_operating_profit',on_delete=models.SET_NULL, null=True)

    income_statement_depreciation = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_depreciation',on_delete=models.SET_NULL, null=True)

    income_statement_other_income = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_other_income',on_delete=models.SET_NULL, null=True)

    income_statement_realised_foreign_exchange_gain_loss  = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_realised_foreign_exchange_gain_loss',on_delete=models.SET_NULL, null=True)

    income_statement_ebit = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_ebit',on_delete=models.SET_NULL, null=True)

    income_statement_interest_including_finance_charges  = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_interest_including_finance_charges',on_delete=models.SET_NULL, null=True)

    income_statement_earnings_before_tax_ebt = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_earnings_before_tax_ebt',on_delete=models.SET_NULL, null=True)

    income_statement_provision_for_income_tax  = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_provision_for_income_tax',on_delete=models.SET_NULL, null=True)

    income_statement_profit_after_tax  = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_profit_after_tax',on_delete=models.SET_NULL, null=True)

    income_statement_ebitda_prc = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_ebitda_prc',on_delete=models.SET_NULL, null=True)

    income_statement_pat_prc = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='income_statement_pat_prc',on_delete=models.SET_NULL, null=True)



    balance_sheet_shareholders_funds_share_capital = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_shareholders_funds_share_capital',on_delete=models.SET_NULL, null=True)

    balance_sheet_shareholders_funds_reserve_and_surplus = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_shareholders_funds_reserve_and_surplus',on_delete=models.SET_NULL, null=True)

    balance_sheet_shareholders_funds_equity_funds_raised = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_shareholders_funds_equity_funds_raised',on_delete=models.SET_NULL, null=True)

    balance_sheet_shareholders_funds_total_shareholder_funds = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_shareholders_funds_total_shareholder_funds',on_delete=models.SET_NULL, null=True)



    balance_sheet_non_current_liabilities_secured_loans = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_liabilities_secured_loans',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_liabilities_unsecured_loans = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_liabilities_unsecured_loans',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_liabilities_deferred_tax_liabilities  = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_liabilities_deferred_tax_liabilities',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_liabilities_long_term_provisions = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_liabilities_long_term_provisions',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_liabilities_other_non_current_liabilities = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_liabilities_other_non_current_liabilities',on_delete=models.SET_NULL, null=True)

    balance_sheet_total_non_current_liabilitie = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_total_non_current_liabilitie',on_delete=models.SET_NULL, null=True)


    balance_sheet_current_liabilities_short_term_borrowings = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_liabilities_short_term_borrowings',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_liabilities_short_term_provisions = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_liabilities_short_term_provisions',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_liabilities_sundry_creditors = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_liabilities_sundry_creditors',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_liabilities_other_current_liabilities = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_liabilities_other_current_liabilities',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_liabilities_total_current_liabilities = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_liabilities_total_current_liabilities',on_delete=models.SET_NULL, null=True)

    balance_sheet_total_liabilities = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_total_liabilities',on_delete=models.SET_NULL, null=True)




    balance_sheet_non_current_assets_gross_fixed_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_gross_fixed_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_less_accumulated_depreciation = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_less_accumulated_depreciation',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_net_fixed_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_net_fixed_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_intangible_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_intangible_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_long_term_loans_and_advances = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_long_term_loans_and_advances',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_long_term_investments = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_long_term_investments',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_deferred_tax_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_deferred_tax_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_other_non_current_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_other_non_current_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_non_current_assets_total_non_current_asset = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_non_current_assets_total_non_current_asset',on_delete=models.SET_NULL, null=True)


    balance_sheet_current_assets_cash = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_assets_cash',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_assets_sundry_debtors = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_assets_sundry_debtors',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_assets_inventory = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_assets_inventory',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_assets_short_term_investments = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_assets_short_term_investments',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_assets_short_term_loans_and_advances = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_assets_short_term_loans_and_advances',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_assets_other_current_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_assets_other_current_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_current_assets_total_current_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_current_assets_total_current_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_total_assets = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_total_assets',on_delete=models.SET_NULL, null=True)

    balance_sheet_check = models.ForeignKey(super_plan_forms_multiple_inputs_xl,related_name='balance_sheet_check',on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField(auto_now_add=True)
























class super_plan_projection(models.Model):
    form_id = models.CharField(max_length=10,null=True)

    #************************* Profit & Loss *****************
    p_revenue_growth_or_amount_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_revenue_growth_or_amount_1',on_delete=models.SET_NULL, null=True)
    p_revenue_growth_or_amount_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_revenue_growth_or_amount_2',on_delete=models.SET_NULL, null=True)
    p_revenue_growth_or_amount_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_revenue_growth_or_amount_3',on_delete=models.SET_NULL, null=True)
    p_revenue_growth_or_amount_4 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_revenue_growth_or_amount_4',on_delete=models.SET_NULL, null=True)
    p_total_revenue_from_operations_services = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_total_revenue_from_operations_services',on_delete=models.SET_NULL, null=True)
    p_other_income_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_income_growth_or_amount',on_delete=models.SET_NULL, null=True)
    p_realised_foreign_exchange_gain_or_loss = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_realised_foreign_exchange_gain_or_loss',on_delete=models.SET_NULL, null=True)
    p_direct_material_units = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_direct_material_units',on_delete=models.SET_NULL, null=True)
    p_direct_material_average_cost_per_unit = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_direct_material_average_cost_per_unit',on_delete=models.SET_NULL, null=True)
    p_total_direct_material_cost = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_total_direct_material_cost',on_delete=models.SET_NULL, null=True)
    p_direct_labour_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_direct_labour_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_direct_labour_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_direct_labour_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_total_labour_cost = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_total_labour_cost',on_delete=models.SET_NULL, null=True)
    p_direct_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_direct_expenses',on_delete=models.SET_NULL, null=True)
    p_other_direct_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_direct_expenses_1',on_delete=models.SET_NULL, null=True)
    p_other_direct_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_direct_expenses_2',on_delete=models.SET_NULL, null=True)
    p_other_direct_expenses_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_direct_expenses_3',on_delete=models.SET_NULL, null=True)
    p_total_product_development_expenses_operating_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_total_product_development_expenses_operating_expenses',on_delete=models.SET_NULL, null=True)
    p_administration_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_administration_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_administration_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_administration_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_administration_employees_total_cost_per_year = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_administration_employees_total_cost_per_year',on_delete=models.SET_NULL, null=True)
    p_selling_and_distribution_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_selling_and_distribution_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_selling_and_distribution_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_selling_and_distribution_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_selling_employees_total_cost_per_year = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_selling_employees_total_cost_per_year',on_delete=models.SET_NULL, null=True)
    p_marketing_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_marketing_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_marketing_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_marketing_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_marketing_employees_total_cost_per_year = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_marketing_employees_total_cost_per_year',on_delete=models.SET_NULL, null=True)
    p_research_and_development_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_research_and_development_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_research_and_development_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_research_and_development_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_research_employees_total_cost_per_year = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_research_employees_total_cost_per_year',on_delete=models.SET_NULL, null=True)
    p_other_employees_1_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_1_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_other_employees_1_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_1_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_other_employees_1_employees_total_cost_per_year = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_1_employees_total_cost_per_year',on_delete=models.SET_NULL, null=True)
    p_other_employees_2_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_2_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_other_employees_2_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_2_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_other_employees_2_employees_total_cost_per_year = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_2_employees_total_cost_per_year',on_delete=models.SET_NULL, null=True)
    p_other_employees_3_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_3_no_of_employees',on_delete=models.SET_NULL, null=True)
    p_other_employees_3_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_3_average_cost_per_employee',on_delete=models.SET_NULL, null=True)
    p_other_employees_3_employees_total_cost_per_year = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_employees_3_employees_total_cost_per_year',on_delete=models.SET_NULL, null=True)
    p_total_employee_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_total_employee_expenses',on_delete=models.SET_NULL, null=True)
    p_rent = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_rent',on_delete=models.SET_NULL, null=True)
    p_telephone_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_telephone_expenses',on_delete=models.SET_NULL, null=True)
    p_electricity = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_electricity',on_delete=models.SET_NULL, null=True)
    p_printing_and_stationery = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_printing_and_stationery',on_delete=models.SET_NULL, null=True)
    p_audit_fees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_audit_fees',on_delete=models.SET_NULL, null=True)
    p_other_administration_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_administration_expenses_1',on_delete=models.SET_NULL, null=True)
    p_other_administration_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_administration_expenses_2',on_delete=models.SET_NULL, null=True)
    p_other_administration_expenses_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_administration_expenses_3',on_delete=models.SET_NULL, null=True)
    p_total_general_administrative_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_total_general_administrative_expenses',on_delete=models.SET_NULL, null=True)
    p_digital_marketing_cost = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_digital_marketing_cost',on_delete=models.SET_NULL, null=True)
    p_sales_commissions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_sales_commissions',on_delete=models.SET_NULL, null=True)
    p_travelling_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_travelling_expenses',on_delete=models.SET_NULL, null=True)
    p_advertisement = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_advertisement',on_delete=models.SET_NULL, null=True)
    p_logistics_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_logistics_expenses',on_delete=models.SET_NULL, null=True)
    p_other_selling_and_marketing_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_selling_and_marketing_expenses_1',on_delete=models.SET_NULL, null=True)
    p_other_selling_and_marketing_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_selling_and_marketing_expenses_2',on_delete=models.SET_NULL, null=True)
    p_other_selling_and_marketing_expenses_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_selling_and_marketing_expenses_3',on_delete=models.SET_NULL, null=True)
    p_total_selling_marketing_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_total_selling_marketing_expenses',on_delete=models.SET_NULL, null=True)
    p_other_expenses_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_expenses_1',on_delete=models.SET_NULL, null=True)
    p_other_expenses_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_other_expenses_2',on_delete=models.SET_NULL, null=True)
    p_income_tax_rate = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_income_tax_rate',on_delete=models.SET_NULL, null=True)


    #************************* Capex *****************

    p_capex_opening_gross = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_capex_opening_gross',on_delete=models.SET_NULL, null=True)
    p_capex_additions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_capex_additions',on_delete=models.SET_NULL, null=True)
    p_capex_additions_intangible = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_capex_additions_intangible',on_delete=models.SET_NULL, null=True)
    p_capex_deletions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_capex_deletions',on_delete=models.SET_NULL, null=True)
    p_closing_gross = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_closing_gross',on_delete=models.SET_NULL, null=True)
    p_accumulated_depreciation = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_accumulated_depreciation',on_delete=models.SET_NULL, null=True)
    p_net_value = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_net_value',on_delete=models.SET_NULL, null=True)
    p_current_depreciation = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_current_depreciation',on_delete=models.SET_NULL, null=True)
    p_capex_average_depreciation_rate = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='p_capex_average_depreciation_rate',on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField(auto_now_add=True)
















class super_plan_forms(models.Model):


    # Form- 1 ----------------------------------------------------------------------------------------- 1 -------------
    theme = models.CharField(max_length=500,null=True)
    currency = models.CharField(max_length=50,null=True)
    denomination  = models.CharField(max_length=50,null=True)
    pack = models.CharField(max_length=100,null=True)

    # Form-2------------------------------------------------------------------------------------- 2 --------------------
    user = models.ForeignKey(User_db, on_delete=models.CASCADE,null=True)
    projection_table=models.ForeignKey(super_plan_projection,on_delete=models.SET_NULL, null=True)
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
    historical_data = models.CharField(max_length=100,null=True)
    historical_xl = models.ImageField(upload_to='superplan-files/',null=True,blank=True)
    historical_xl_data = models.ForeignKey(super_plan_form_xl_input, on_delete=models.CASCADE,null=True)


    # Form-10-------------------------------------------------------------------------------------------------10 ---------
    profit_and_loss_years = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='profit_and_loss_years',on_delete=models.SET_NULL, null=True)

    revenue_growth_or_amount_1 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_1',on_delete=models.SET_NULL, null=True)
    
    revenue_growth_or_amount_2 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_2',on_delete=models.SET_NULL, null=True)
    
    revenue_growth_or_amount_3 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_3',on_delete=models.SET_NULL, null=True)

    revenue_growth_or_amount_4 = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='revenue_growth_or_amount_4',on_delete=models.SET_NULL, null=True)

    other_income_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_income_growth_or_amount', on_delete=models.SET_NULL, null=True)
    
    realised_foreign_exchange_gain_or_loss = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='realised_foreign_exchange_gain_or_loss', on_delete=models.SET_NULL, null=True)
    
    direct_material_units = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_material_units', on_delete=models.SET_NULL, null=True)

    direct_material_average_cost_per_unit =models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_material_average_cost_per_unit', on_delete=models.SET_NULL, null=True) 

    direct_labour_no_of_employees = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_labour_no_of_employees', on_delete=models.SET_NULL, null=True)

    direct_labour_average_cost_per_employee = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_labour_average_cost_per_employee', on_delete=models.SET_NULL, null=True)
    
    direct_expenses = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='direct_expenses', on_delete=models.SET_NULL, null=True)

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



    # Form- 11 ----------------------------------------------------------------------------------------- 11 -------------

    capex_years = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_years',on_delete=models.SET_NULL, null=True)

    capex_opening_gross = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_opening_gross',on_delete=models.SET_NULL, null=True)
    
    capex_additions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_additions',on_delete=models.SET_NULL, null=True)

    capex_additions_intangible = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_additions_intangible',on_delete=models.SET_NULL, null=True)
    
    capex_deletions = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_deletions',on_delete=models.SET_NULL, null=True)

    capex_average_depreciation_rate = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='capex_average_depreciation_rate',on_delete=models.SET_NULL, null=True)

    current_fillup_position = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    # Form -12 ----------------------------------------------------------------------------------------------12 ----------
    
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
    
    long_term_provisions_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_provisions_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_non_current_liabilities_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_non_current_liabilities_growth_or_amount',on_delete=models.SET_NULL, null=True)

    short_term_borrowings_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_borrowings_growth_or_amount',on_delete=models.SET_NULL, null=True)

    short_term_provisions_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_provisions_growth_or_amount',on_delete=models.SET_NULL, null=True)

    sundry_creditors_no_of_days = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='sundry_creditors_no_of_days',on_delete=models.SET_NULL, null=True)

    other_current_liabilities_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_current_liabilities_growth_or_amount',on_delete=models.SET_NULL, null=True)

    intangible_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='intangible_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    long_term_loans_and_advances_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_loans_and_advances_growth_or_amount',on_delete=models.SET_NULL, null=True)

    long_term_investments_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='long_term_investments_growth_or_amount',on_delete=models.SET_NULL, null=True)

    deferred_tax_assets = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='deferred_tax_assets',on_delete=models.SET_NULL, null=True)

    other_non_current_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_non_current_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    sundry_debtors_no_of_days = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='sundry_debtors_no_of_days',on_delete=models.SET_NULL, null=True)

    inventory_no_of_days = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='inventory_no_of_days',on_delete=models.SET_NULL, null=True)

    short_term_investments_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_investments_growth_or_amount',on_delete=models.SET_NULL, null=True)

    short_term_loans_and_advances_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='short_term_loans_and_advances_growth_or_amount',on_delete=models.SET_NULL, null=True)

    other_current_assets_growth_or_amount = models.ForeignKey(super_plan_forms_multiple_inputs,related_name='other_current_assets_growth_or_amount',on_delete=models.SET_NULL, null=True)

    







    def __str__(self):
        return self.user.name







#-----------------------------------------------------------------------------------------------------------------













