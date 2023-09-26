from flask import Flask, request, jsonify
from flask import Flask
from flask_cors import CORS
import numpy as np
import sympy as sp

import metodos.biseccion as biseccion
import metodos.jacobi as jacobi
import metodos.newton_raphson as newton
import metodos.polinomio_lagrange as polinomio
import metodos.punto_fijo as puntofijo
import metodos.secante as secante
import metodos.simpson as simpson
import metodos.trapezoidal as trapezoidal
import metodos.sedial as sedial


app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#biseccion
@app.route('/api/biseccion', methods=['POST'])
def metodobiseccion():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            a = data['a']
            b = data['b']
            response=biseccion.bisection_solver(ecuacion,a,b)
            return jsonify({"response":response})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        

#jacobi
@app.route('/api/jacobi', methods=['POST'])
def metodojacobi():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            resultados = data['resultados']
            xi = data['xi']
            
            
            response=jacobi.jacobi(ecuacion,resultados,xi)
            response_list = response.tolist() if isinstance(response, np.ndarray) else response
            return jsonify({"response":response_list})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400

#sedial
@app.route('/api/sedial', methods=['POST'])
def metodosedial():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            resultados = data['resultados']
            xi = data['xi']
            
            
            response=sedial.gauss_seidel(ecuacion,resultados,xi)
            response_list = response.tolist() if isinstance(response, np.ndarray) else response
            return jsonify({"response":response_list})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        

#newton
@app.route('/api/newton', methods=['POST'])
def metodonewton():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            xi = data['xi']
            response = newton.newton_raphson(ecuacion,"x",xi)
            return jsonify({"response": f"{response:.6f}"})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        


@app.route('/api/polinomio', methods=['POST'])
def metodopolinomio():
    if request.method == 'POST':
        data = request.json  
        if 'valoresx' in data:
            valores_x = data['valoresx']
            valores_y = data['valoresy']
            response = polinomio.graficar_polinomio(valores_x, valores_y)
            return jsonify({"response":str(response)})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        


@app.route('/api/puntofijo', methods=['POST'])
def metodopuntofijo():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']

            response= puntofijo.punto_fijo_inicio(ecuacion)
            return jsonify({"response": response})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        

        
@app.route('/api/secante', methods=['POST'])
def metodosecante():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            x = data['x0']
            xi = data['x1']
            response=secante.secante(ecuacion,x,xi)
            return jsonify({"response":f"{response:.6f}"})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        

        
@app.route('/api/simpson', methods=['POST'])
def metodosimpson():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            inferior = data['inferior']
            superior = data['superior']
            intervalos = data['intervalos']

            response=simpson.simpson(ecuacion,inferior,superior,intervalos)

            return jsonify({"response":f"{response:.6f}"})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        

        
@app.route('/api/trapezoidal', methods=['POST'])
def metodotrapezoidal():
    if request.method == 'POST':
        data = request.json  
        if 'ecuacion' in data:
            ecuacion = data['ecuacion']
            inferior = data['inferior']
            superior = data['superior']
            intervalos = data['intervalos']

            response=trapezoidal.trapezoidal(ecuacion,inferior,superior,intervalos)

            return jsonify({"response":f"{response:.6f}"})
        else:
            return jsonify({'error': 'El campo "texto" es requerido'}), 400
        

        





if __name__ == '__main__':
    app.run(debug=True)