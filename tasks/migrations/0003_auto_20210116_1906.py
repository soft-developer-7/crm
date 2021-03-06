# Generated by Django 3.1.1 on 2021-01-16 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_super_plan_forms_historical_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='capex_additions_intangible_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='capex_additions_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='capex_deletions_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='deferred_tax_assets_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='intangible_assets_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='long_term_investments_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='long_term_loans_and_advances_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='long_term_provisions_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='other_current_assets_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='other_current_liabilities_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='other_income_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='other_non_current_assets_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='other_non_current_liabilities_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='realised_foreign_exchange_gain_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='revenue_growth_1_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='revenue_growth_2_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='revenue_growth_3_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='revenue_growth_4_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='short_term_borrowings_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='short_term_investments_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='short_term_loans_and_advances_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='short_term_provisions_growth_or',
        ),
        migrations.RemoveField(
            model_name='super_plan_forms',
            name='working_capital',
        ),
    ]
