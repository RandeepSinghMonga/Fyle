from flask import Flask, request, render_template, redirect,jsonify, Response
import os,sys,json,logging
import sqlite3
app = Flask('Fyle')

@app.route('/ifsc/<ifsc_code>')
def get_branch_details(ifsc_code):
	conn = sqlite3.connect('fyle.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM bank_branches where ifsc=?;", (ifsc_code,) )
	branch = cursor.fetchall()
	conn.commit()
	return json.dumps(branch)

@app.route('/bank_name/<bank_name>/city/<city>')
def get_all_branches(bank_name,city):
	conn = sqlite3.connect('fyle.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM bank_branches where bank_name=? and city=?;", (bank_name,city,) )
	branches = cursor.fetchall()
	conn.commit()
	return json.dumps(branches)

if __name__=='__main__':
	logging.basicConfig(filename='error.log',level=logging.DEBUG)
	app.run(debug=True,host='0.0.0.0')