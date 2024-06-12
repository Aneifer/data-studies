import plotly.graph_objects as go

# Daten
generationen = ["Gen Z (1997+)", "Millennials (1981-1996)", "Gen X (1965-1980)", "Baby Boomers (1946-1964)"][::-1]
deutschland = [22, 10, 10, 5][::-1]
weltweit = [18, 10, 6, 4][::-1]

# Farben
deutschland_farbe = 'rgb(255, 182, 193)'  # Light Rosé
weltweit_farbe = 'rgb(173, 216, 230)'  # Light Blue

# Diagramm erstellen
fig = go.Figure()

# Balken für Deutschland hinzufügen
fig.add_trace(go.Bar(
    y=generationen,
    x=deutschland,
    name='Deutschland',
    orientation='h',
    marker_color=deutschland_farbe,
    hovertemplate='%{x}%<br><b>Deutschland</b><extra></extra>'
))

# Balken für Weltweit hinzufügen
fig.add_trace(go.Bar(
    y=generationen,
    x=weltweit,
    name='Weltweit',
    orientation='h',
    marker_color=weltweit_farbe,
    hovertemplate='%{x}%<br><b>Weltweit</b><extra></extra>'
))

# Layout für den Dark Mode aktualisieren
fig.update_layout(
    title={
        'text': 'Prozentsatz der Menschen, die sich als LGBT+ identifizieren nach Generation (Deutschland vs Weltweit)',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    annotations=[
        {
            'text': 'Erstellt von: Autorin<br>Quelle: Ipsos Global Advisor Studie',
            'xref': 'paper',
            'yref': 'paper',
            'x': 0,
            'y': -0.2,
            'showarrow': False,
            'font': {
                'size': 12,
                'color': 'white'
            }
        }
    ],
    xaxis=dict(
        title='Prozentsatz',
        titlefont_size=16,
        tickfont_size=14,
        color='white'
    ),
    yaxis=dict(
        title='Generation',
        titlefont_size=16,
        tickfont_size=14,
        color='white'
    ),
    legend=dict(
        x=0.02,
        y=1.05,
        bgcolor='rgba(0,0,0,0)',
        bordercolor='rgba(255,255,255,0.5)',
        font=dict(
            color='white'
        )
    ),
    barmode='group',
    bargap=0.15,
    plot_bgcolor='rgb(17, 17, 17)',
    paper_bgcolor='rgb(17, 17, 17)',
    font=dict(
        color='white'
    )
)

# LGBT+ Symbol hinzufügen
fig.add_layout_image(
    dict(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Flag_of_LGBT.svg/1200px-Flag_of_LGBT.svg.png",
        xref="paper", yref="paper",
        x=1, y=1,
        sizex=0.15, sizey=0.15,
        xanchor="right", yanchor="bottom"
    )
)

# Diagramm anzeigen
fig.show()
