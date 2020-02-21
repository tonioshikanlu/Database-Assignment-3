from flask import render_template
from flask import request
from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE


# def Sailors(conn):
# 	userInput = request.form["boat-name"]
# 	return execute(conn, "SELECT s.name FROM Sailors AS s INNER JOIN Voyagers INNER JOIN Boats AS b WHERE  b.name = (%s)", (userInput))

def sailors_who_sailed(conn):
	userInput = request.form.get("boat-name")
	print (userInput)
	return execute(conn, "SELECT bid FROM Boats WHERE name = (?)", (userInput,))

def views(bp):
	@bp.route("/sailors/who-sailed",  methods=['GET', 'POST'])
	def _get_all_sailors_who_sailed():
		
		with get_db() as conn:
			rows = sailors_who_sailed(conn)
		return render_template("table.html", name="sailors", rows=rows)