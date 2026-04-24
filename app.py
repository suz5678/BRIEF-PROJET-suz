import plotly.express as px
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv"
donnees = pd.read_csv(url)

print(donnees.columns)

ventes_produit = donnees.groupby('produit')['qte'].sum().reset_index()

fig1 = px.bar(
    ventes_produit,
    x='produit',
    y='qte',
    title='Ventes par produit',
    color='produit'
)

fig1.write_html('ventes-par-produit.html')

donnees['CA'] = donnees['qte'] * donnees['prix']

ca_produit = donnees.groupby('produit')['CA'].sum().reset_index()

fig2 = px.bar(
    ca_produit,
    x='produit',
    y='CA',
    title="Chiffre d'affaires par produit",
    color='produit'
)

fig2.write_html('ca-par-produit.html')

fig3 = px.pie(
    donnees,
    values='qte',
    names='region',
    title='Quantité vendue par région'
)

fig3.write_html('ventes-par-region.html')

print("✅ Tous les graphiques ont été générés avec succès !")
