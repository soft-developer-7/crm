# Generated by Django 3.1.1 on 2020-11-30 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20201128_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super_plan_forms',
            name='cash',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cash', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='company_owned_land_and_building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_owned_land_and_building', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='depreciation_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='depreciation_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='fund_requirement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fund_requirement', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='gross_fixed_assets_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gross_fixed_assets_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='industry_type',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='intangible_assets_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intangible_assets_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='inventory_no_of_days_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventory_no_of_days_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='less_accumulated_depreciation_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='less_accumulated_depreciation_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='long_term_investments_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='long_term_investments_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='long_term_loans_and_advances_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='long_term_loans_and_advances_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='long_term_provisions_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='long_term_provisions_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='net_fixed_assets_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='net_fixed_assets_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='other_current_assets_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_current_assets_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='other_current_liabilities_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_current_liabilities_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='other_fixed_assets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_fixed_assets', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='other_non_current_assets_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_non_current_assets_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='other_non_current_liabilities_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_non_current_liabilities_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='reserves_and_surplus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserves_and_surplus', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='secured_loans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secured_loans', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='share_capital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='share_capital', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='short_term_borrowings_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='short_term_borrowings_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='short_term_investments_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='short_term_investments_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='short_term_loans_and_advances_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='short_term_loans_and_advances_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='short_term_provisions_growth_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='short_term_provisions_growth_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='sundry_creditors_no_of_days_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sundry_creditors_no_of_days_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='sundry_debtors_no_of_days_or_amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sundry_debtors_no_of_days_or_amount', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_assets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_assets', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_capex_expense',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_capex_expense', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_current_assets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_current_assets', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_current_liabilities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_current_liabilities', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_liabilities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_liabilities', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_non_current_assets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_non_current_assets', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_non_current_liabilities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_non_current_liabilities', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='total_shareholder_funds',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='total_shareholder_funds', to='tasks.super_plan_forms_multiple_inputs'),
        ),
        migrations.AlterField(
            model_name='super_plan_forms',
            name='unsecured_loans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unsecured_loans', to='tasks.super_plan_forms_multiple_inputs'),
        ),
    ]
