import plotly.graph_objects as go

# Daten
generationen = ["Gen Z<br>(1997+)", "Millennials<br>(1981-1996)", "Gen X<br>(1965-1980)", "Baby Boomers<br>(1946-1964)"][::-1]
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
    hovertemplate='<b>%{x}%</b><b> Deutschland<br>%{y}<br></b><extra></extra>',
    hoverlabel=dict(font_size=26)
))

# Balken für Weltweit hinzufügen
fig.add_trace(go.Bar(
    y=generationen,
    x=weltweit,
    name='Weltweit',
    orientation='h',
    marker_color=weltweit_farbe,
    hovertemplate='<b>%{x}%</b><b> Weltweit<br>%{y}<br></b><extra></extra>',
    hoverlabel=dict(font_size=26)
))

# Layout für den Dark Mode aktualisieren
fig.update_yaxes(
    tickmode='array',
    tickvals=[0, 1, 2, 3],
    ticktext=["Baby Boomers  <br>(1946-1964)  ", "Gen X  <br>(1965-1980)  ", "Millennials  <br>(1981-1996)  ", "Gen Z  <br>(1997+)  "],
    ticklabelposition="outside",
    ticklen=3,
    zeroline=False,
    showline=False,
    showgrid=False,
    title_standoff=10 
)


fig.update_layout(
    title={
        'text': 'Prozentsatz der Menschen, die sich als LGBT+ identifizieren nach Generation. <br> Deutschland vs. Weltweit.',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 34, 'color': 'white'}
    },
    annotations=[
        {
            'text': 'Erstellt von: Anna Neifer <br>Quelle: Ipsos Global Advisor Studie',
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.9,
            'y': -0.1,
            'showarrow': False,
            'font': {'size': 12, 'color': 'white'}
        }
    ],
    xaxis=dict(
        domain=[0.1, 1], 
        title_text='',
        tickfont_size=22,
        fixedrange=True,
        color='white',
        showline=False,
        showgrid=False,
        showticklabels=False
    ),
   yaxis=dict(
        title_text='',
        tickfont=dict(size=32, color='white'),
        fixedrange=True,
        showticklabels=True,
         # Adjust this value to increase the space
    ),
    legend=dict(
        x=0.9,  # Koordinaten anpassen, um die Legende zu verschieben
        y=-0.1,
        bgcolor='rgba(0,0,0,0)',
        bordercolor='rgba(255,255,255,0.5)',
        font=dict(color='white')
    ),
    margin=dict(l=150, r=50, t=100, b=100),  # Erhöhter linker Rand für mehr Platz
    barmode='group',
    bargap=0.15,
    plot_bgcolor='rgb(17, 17, 17)',
    paper_bgcolor='rgb(17, 17, 17)',
    font=dict(color='white')
)

# Diagramm anzeigen
fig.show()
