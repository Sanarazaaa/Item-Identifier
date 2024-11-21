import plotly.express as px
import plotly.graph_objects as go

def create_confidence_gauge(confidence):
    """Create confidence gauge chart"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = confidence * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Confidence"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 75], 'color': "gray"},
                {'range': [75, 100], 'color': "darkgray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    return fig

def create_impact_metrics(recycled_items):
    """Create environmental impact visualization"""
    # Example impact calculations
    co2_saved = recycled_items * 0.5  # kg of CO2
    water_saved = recycled_items * 2   # liters of water
    energy_saved = recycled_items * 1.5 # kWh
    
    fig = go.Figure()
    
    categories = ['CO2 Saved (kg)', 'Water Saved (L)', 'Energy Saved (kWh)']
    values = [co2_saved, water_saved, energy_saved]
    
    fig.add_trace(go.Bar(
        x=categories,
        y=values,
        marker_color=['#2ecc71', '#3498db', '#f1c40f']
    ))
    
    fig.update_layout(
        title="Your Environmental Impact",
        showlegend=False,
        height=400
    )
    
    return fig