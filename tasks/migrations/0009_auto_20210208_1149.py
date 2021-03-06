# Generated by Django 3.1.1 on 2021-02-08 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20210205_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_depreciation',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_earnings_before_tax_ebt',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_ebit',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_ebitda_operating_profit',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_employee_cost',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_general_administrative_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_interest_including_finance_charges',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_other_expenses_1',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_other_expenses_2',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_other_income',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_profit_after_tax',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_provision_for_income_tax',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_realised_foreign_exchange_gain_loss',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_selling_marketing_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_stream_1',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_stream_2',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_stream_3',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_stream_4',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_total_operating_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_analysis_as_of_revenue_total_revenue_from_operations_services',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_depreciation',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_earnings_before_tax_ebt',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_ebit',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_ebitda_operating_profit',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_employee_cost',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_foreign_exchange_gain_loss',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_general_administrative_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_interest_including_finance_charges',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_other_expenses_1',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_other_expenses_2',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_other_income',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_profit_after_tax',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_provision_for_income_tax',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_selling_marketing_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_stream_1',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_stream_2',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_stream_3',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_stream_4',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_total_operating_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_growth_analysis_yoy_total_revenue_from_operations_services',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_depreciation',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_earnings_before_tax_ebt',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_ebit',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_ebitda_operating_profit',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_ebitda_perc',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_employee_cost',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_financial_leverage',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_general_administrative_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_interest_cover',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_interest_including_finance_charges',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_other_expenses_1',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_other_expenses_2',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_other_income',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_pat_perc',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_product_development_expenses_operating_expenses_raw_material',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_profit_after_tax',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_provision_for_income_tax',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_realised_foreign_exchange_gain_loss',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_selling_marketing_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_stream_1',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_stream_2',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_stream_3',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_stream_4',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_total_operating_expenses',
        ),
        migrations.RemoveField(
            model_name='super_plan_projection',
            name='is_particulars_total_revenue_from_operations_services',
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_depreciation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_depreciation', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_earnings_before_tax_ebt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_earnings_before_tax_ebt', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_ebit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_ebit', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_ebitda_operating_profit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_ebitda_operating_profit', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_employee_cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_employee_cost', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_general_administrative_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_general_administrative_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_interest_including_finance_charges',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_interest_including_finance_charges', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_other_expenses_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_other_expenses_1', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_other_expenses_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_other_expenses_2', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_other_income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_other_income', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_profit_after_tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_profit_after_tax', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_provision_for_income_tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_provision_for_income_tax', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_selling_marketing_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_selling_marketing_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_stream_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_stream_1', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_stream_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_stream_2', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_stream_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_stream_3', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_stream_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_stream_4', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_total_operating_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_total_operating_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_analysis_as_of_revenue_total_revenue_from_operations_services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_analysis_as_of_revenue_total_revenue_from_operations_services', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_depreciation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_depreciation', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_earnings_before_tax_ebt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_earnings_before_tax_ebt', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_ebit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_ebit', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_ebitda_operating_profit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_ebitda_operating_profit', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_employee_cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_employee_cost', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_foreign_exchange_gain_loss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_foreign_exchange_gain_loss', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_general_administrative_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_general_administrative_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_interest_including_finance_charges',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_interest_including_finance_charges', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_other_expenses_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_other_expenses_1', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_other_expenses_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_other_expenses_2', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_other_income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_other_income', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_profit_after_tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_profit_after_tax', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_provision_for_income_tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_provision_for_income_tax', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_selling_marketing_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_selling_marketing_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_stream_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_stream_1', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_stream_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_stream_2', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_stream_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_stream_3', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_stream_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_stream_4', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_total_operating_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_total_operating_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_growth_analysis_yoy_total_revenue_from_operations_services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_growth_analysis_yoy_total_revenue_from_operations_services', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_depreciation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_depreciation', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_earnings_before_tax_ebt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_earnings_before_tax_ebt', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_ebit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_ebit', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_ebitda_operating_profit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_ebitda_operating_profit', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_ebitda_perc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_ebitda_perc', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_employee_cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_employee_cost', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_financial_leverage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_financial_leverage', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_general_administrative_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_general_administrative_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_interest_cover',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_interest_cover', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_interest_including_finance_charges',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_interest_including_finance_charges', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_other_expenses_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_other_expenses_1', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_other_expenses_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_other_expenses_2', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_other_income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_other_income', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_pat_perc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_pat_perc', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_product_development_expenses_operating_expenses_raw_material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_product_development_expenses_operating_expenses_raw_material', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_profit_after_tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_profit_after_tax', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_provision_for_income_tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_provision_for_income_tax', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_realised_foreign_exchange_gain_loss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_realised_foreign_exchange_gain_loss', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_selling_marketing_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_selling_marketing_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_stream_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_stream_1', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_stream_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_stream_2', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_stream_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_stream_3', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_stream_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_stream_4', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_total_operating_expenses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_total_operating_expenses', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AddField(
            model_name='super_plan_projection',
            name='ins_particulars_total_revenue_from_operations_services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ins_particulars_total_revenue_from_operations_services', to='tasks.super_plan_forms_multiple_inputs'),
        ),
    ]
