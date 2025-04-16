from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Default parameters
DEFAULTS = {
    'jobs_displaced': 500_000_000,  # 500 million
    'avg_wage': 16_000,  # $16,000
    'labor_tax_rate': 17.7,  # 17.7%
    'automation_tax_per_job': 10_000,  # $10,000
    'ubi_payment': 10_000,  # $10,000
    'efficiency_savings_pct': 2.285,  # 2.285% of GDP ($2.4T / $105T)
    'ai_gdp_growth': 15.0,  # 15% GDP growth due to AI
    'total_workforce': 3_650_000_000,  # 3.65 billion
    'baseline_gdp': 105_000_000_000_000,  # $105 trillion
}

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize with defaults
    params = DEFAULTS.copy()
    results = {}
    
    if request.method == 'POST':
        # Update parameters from form inputs
        params['jobs_displaced'] = int(float(request.form.get('jobs_displaced', DEFAULTS['jobs_displaced'] / 1_000_000)) * 1_000_000)
        params['avg_wage'] = float(request.form.get('avg_wage', DEFAULTS['avg_wage']))
        params['labor_tax_rate'] = float(request.form.get('labor_tax_rate', DEFAULTS['labor_tax_rate']))
        params['automation_tax_per_job'] = float(request.form.get('automation_tax_per_job', DEFAULTS['automation_tax_per_job']))
        params['ubi_payment'] = float(request.form.get('ubi_payment', DEFAULTS['ubi_payment']))
        params['efficiency_savings_pct'] = float(request.form.get('efficiency_savings_pct', DEFAULTS['efficiency_savings_pct']))
        params['ai_gdp_growth'] = float(request.form.get('ai_gdp_growth', DEFAULTS['ai_gdp_growth']))
        # Handle total_workforce: convert from millions to actual number
        params['total_workforce'] = int(float(request.form.get('total_workforce', DEFAULTS['total_workforce'] / 1_000_000)) * 1_000_000)
        params['baseline_gdp'] = DEFAULTS['baseline_gdp']

    # Calculations
    # Total GDP after AI growth
    total_gdp = params['baseline_gdp'] * (1 + params['ai_gdp_growth'] / 100)
    
    # Labor income loss
    labor_income_loss = params['jobs_displaced'] * params['avg_wage']
    
    # Labor tax loss
    labor_tax_loss = labor_income_loss * (params['labor_tax_rate'] / 100)
    
    # Automation tax revenue
    automation_tax_revenue = params['jobs_displaced'] * params['automation_tax_per_job']
    
    # Total revenue change
    total_revenue_change = automation_tax_revenue - labor_tax_loss
    
    # Efficiency savings in dollars
    efficiency_savings = (params['efficiency_savings_pct'] / 100) * total_gdp
    
    # UBI cost
    ubi_cost = params['jobs_displaced'] * params['ubi_payment']
    
    # Net spending change
    spending_change = ubi_cost - efficiency_savings
    
    # Net fiscal impact
    net_fiscal_impact = total_revenue_change - spending_change

    # Convert to percentages of total GDP
    results = {
        'total_gdp': total_gdp,
        'labor_income_loss': labor_income_loss,
        'labor_income_loss_pct': (labor_income_loss / total_gdp) * 100 if total_gdp else 0,
        'labor_tax_loss': labor_tax_loss,
        'labor_tax_loss_pct': (labor_tax_loss / total_gdp) * 100 if total_gdp else 0,
        'automation_tax_revenue': automation_tax_revenue,
        'automation_tax_pct': (automation_tax_revenue / total_gdp) * 100 if total_gdp else 0,
        'total_revenue_change': total_revenue_change,
        'total_revenue_change_pct': (total_revenue_change / total_gdp) * 100 if total_gdp else 0,
        'efficiency_savings': efficiency_savings,
        'efficiency_savings_pct': params['efficiency_savings_pct'],
        'ubi_cost': ubi_cost,
        'ubi_cost_pct': (ubi_cost / total_gdp) * 100 if total_gdp else 0,
        'spending_change': spending_change,
        'spending_change_pct': (spending_change / total_gdp) * 100 if total_gdp else 0,
        'net_fiscal_impact': net_fiscal_impact,
        'net_fiscal_impact_pct': (net_fiscal_impact / total_gdp) * 100 if total_gdp else 0,
    }

    # Data for Chart.js
    chart_data = {
        'labels': ['Labor Tax Loss', 'Automation Tax', 'Revenue Change', 'Efficiency Savings', 'UBI Cost', 'Spending Change', 'Net Fiscal Impact'],
        'values': [
            -results['labor_tax_loss'],
            results['automation_tax_revenue'],
            results['total_revenue_change'],
            results['efficiency_savings'],
            -results['ubi_cost'],
            -results['spending_change'],
            results['net_fiscal_impact']
        ]
    }

    return render_template(
        'index.html',
        params=params,
        results=results,
        chart_data=json.dumps(chart_data),
        baseline_gdp=DEFAULTS['baseline_gdp']
    )

if __name__ == '__main__':
    app.run(debug=True)