import plotly.graph_objects as go
import pandas as pd

# Daten vorbereiten
data = {
    'Generation_Land': [
        "Gen Z (1997+)", "Gen Z (1997+)",
        "Millennials (1981-1996)", "Millennials (1981-1996)",
        "Gen X (1965-1980)", "Gen X (1965-1980)",
        "Baby Boomers (1946-1964)", "Baby Boomers (1946-1964)"
    ],
    'Land': ["Weltweit", "Deutschland", "Weltweit", "Deutschland", "Weltweit", "Deutschland", "Weltweit", "Deutschland"],
    'Prozentsatz': [18, 22, 10, 10, 6, 10, 4, 5],
    'Generation': [
        "Gen Z", "Gen Z",
        "Millennials", "Millennials",
        "Gen X", "Gen X",
        "Baby Boomers", "Baby Boomers"
    ]
}

df = pd.DataFrame(data)

# Grunddiagramm erstellen
fig = go.Figure()

# Initialer leeren Trace hinzufügen, um die Balken zu initialisieren
fig.add_trace(go.Bar(
    x=[0],
    y=["Gen Z (1997+)", "Gen Z (1997+)", "Millennials (1981-1996)", "Millennials (1981-1996)", "Gen X (1965-1980)", "Gen X (1965-1980)", "Baby Boomers (1946-1964)", "Baby Boomers (1946-1964)"],
    orientation='h',
    marker_color='rgb(255, 182, 193)',
    name='Deutschland'
))
fig.add_trace(go.Bar(
    x=[0],
    y=["Gen Z (1997+)", "Gen Z (1997+)", "Millennials (1981-1996)", "Millennials (1981-1996)", "Gen X (1965-1980)", "Gen X (1965-1980)", "Baby Boomers (1946-1964)", "Baby Boomers (1946-1964)"],
    orientation='h',
    marker_color='rgb(173, 216, 230)',
    name='Weltweit'
))

# Layout des Diagramms anpassen
fig.update_layout(
    title='Prozentsatz der Menschen, die sich als LGBT+ identifizieren nach Generation. <br> Deutschland vs. Weltweit.',
    xaxis=dict(
        domain=[0.1, 1], 
        tickfont_size=22,
        fixedrange=True,
        color='white',
        showline=False,
        showgrid=False,
        showticklabels=True,
        range=[0, 25]
    ),
    yaxis=dict(
        title_text='',
        tickfont=dict(size=32, color='white'),
        fixedrange=True,
        showticklabels=True,
        categoryorder='array',
        categoryarray=[
            "Gen Z (1997+)", "Gen Z (1997+)",
            "Millennials (1981-1996)", "Millennials (1981-1996)",
            "Gen X (1965-1980)", "Gen X (1965-1980)",
            "Baby Boomers (1946-1964)", "Baby Boomers (1946-1964)"
        ]
    ),
    legend=dict(
        x=0.9,
        y=-0.1,
        traceorder='reversed',  # Legende umdrehen, damit "Weltweit" oben steht
        bgcolor='rgba(0,0,0,0)',
        bordercolor='rgba(255,255,255,0.5)',
        font=dict(color='white')
    ),
    margin=dict(l=150, r=50, t=100, b=100),
    plot_bgcolor='rgb(17, 17, 17)',
    paper_bgcolor='rgb(17, 17, 17)',
    font=dict(color='white'),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.0,
    updatemenus=[{
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 1000, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 500, 'easing': 'linear'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }]
)

# Frames für die Animation erstellen
frames = []
for i, gen in enumerate(df['Generation'].unique()):
    filtered_df = df[df['Generation'].isin(df['Generation'].unique()[:i+1])]
    frames.append(go.Frame(
        data=[
            go.Bar(
                x=filtered_df[filtered_df['Land'] == 'Deutschland']['Prozentsatz'],
                y=filtered_df[filtered_df['Land'] == 'Deutschland']['Generation_Land'],
                orientation='h',
                marker_color='rgb(255, 182, 193)',
                name='Deutschland'
            ),
            go.Bar(
                x=filtered_df[filtered_df['Land'] == 'Weltweit']['Prozentsatz'],
                y=filtered_df[filtered_df['Land'] == 'Weltweit']['Generation_Land'],
                orientation='h',
                marker_color='rgb(173, 216, 230)',
                name='Weltweit'
            )
        ],
        name=gen
    ))

fig.frames = frames

# Diagramm anzeigen
fig.show()

# Diagramm speichern
fig.write_html('/home/an/git/Aneifer/data-studies/24_lgbtq_animated_plotly_graphics.html', full_html=True)
