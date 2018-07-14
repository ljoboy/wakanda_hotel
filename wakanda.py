#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash,check_password_hash
from Client import *
from Chambre import *


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hotel")
def hotel():
    return render_template('hotel.html')


@app.route("/hotel/add_client", methods=['GET', 'POST'])
def add_client():
    if request.method == 'GET':
        infos = [("nom", "text"), ("prenom", "text"), ("postnom", "text"), ("email", "email"), ("téléphone", "tel"), ("nationalite", "text"), ("profession", "text"), ("sexe", "radio")]
        return render_template('hotel/add_client.html', infos=infos)
    elif request.method == 'POST':
        ajouter_client(request.values.get("nom"),request.values.get("postnom"),request.values.get("prenom"),request.values.get("email"),request.values.get("téléphone"),request.values.get("nationalite"),request.values.get("profession"),request.values.get("sexe"))
        return redirect("/hotel/all_clients")


@app.route("/hotel/all_clients")
def all_clients():
    clients = affichage_client()
    return render_template('hotel/liste_clients.html', clients=clients)


@app.route("/hotel/modif_client/<client_id>", methods=['GET', 'POST'])
def modif_client(client_id):
    if request.method == 'GET':
        if client_id != 0:
            client = recup_client_par_id(client_id)
            return render_template("hotel/modif_client.html", client=client, id_client=client_id)
    elif request.method == 'POST':
        modifier_client(request.values.get("id"), request.values)
    return redirect("hotel/all_client")


@app.route("/hotel/add_chambre", methods=['GET', 'POST'])
def add_chambre():
    if request.method == "GET":
        types = afficher_type()
        return render_template("hotel/add_chambre.html", types=types)
    elif request.method == 'POST':
        ajouter_chambre(request.values.get("id_type"), request.values.get("nom"), request.values.get('details'))
        redirect("/hotel/liste_chambres")


@app.route("/hotel/liste_chambres")
def all_chambre():
    chambres = chambre_type()
    return render_template("hotel/all_chambres.html", chambres=chambres)


@app.route("/hotel/add_type_chambre", methods=["GET", 'POST'])
def add_type_chambre():
    if request.method == 'GET':
        return render_template("hotel/add_type.html")
    elif request.method == 'POST':
        ajouter_type(request.values.get("prix"), request.values.get("nom"), request.values.get("details"), request.values.get("nbPerso"))
    redirect('/hotel/liste_chambres')


@app.route("/hotel/liste_type")
def liste_type():
    types = afficher_type()
    return render_template("hotel/all_types.html", types=types)


@app.route("/hotel/reservation", methods=['GET', 'POST'])
def reservation():
    if request.method == 'GET':
        chambres = chambre_dispo()
        clients = affichage_client()
        return render_template("hotel/reservation.html", chambres=chambres, clients=clients)
    elif request.method == 'POST':
        ajouter_reservation(request.values.get("id_client"), request.values.get("id_chambre"), request.values.get("check_in"), request.values.get("check_out"), request.values.get("prix"), request.values.get("details"))
        indispo_chambre(request.values.get("id_chambre"))
    return redirect("/hotel")


@app.route("/resto")
def resto():
    return render_template('resto.html')


@app.route("/team")
def team():
    return render_template("team.html")


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("404.html"), 404


@property
def password(self):
    raise AttributeError('Attribut en écriture seul')


@password.setter
def password(self, password):
    self.password_hash = generate_password_hash(password)


def verify_password(self, password):
    return check_password_hash(self.password_hash, password)


app.run(debug=True)
