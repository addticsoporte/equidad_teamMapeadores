from datetime import datetime
from flask import Flask, render_template, send_from_directory
import os
import json
from markupsafe import escape
from flask import Flask, session
from flask_session import Session

from CantidadNivelResponsabilidad import *
from CantidadPorInstitucion import *
from CantidadPorPuesto import *
from CantidadPorTipoArea import *
from CantidadPorTipoProcedimiento import *

from ClasificacionInstitucion import *
from ClasificacionNivelResponsabilidad import *
from ClasificaciónPuesto import *
from ClasificaciónTipoArea import *
from ClasificacionTipoProcedimiento import *

from InstitucionesAnios import *
from InstitucionesPuesto import *

from NivelResponsabilidad import *
from TipoArea import *
from TipoProcedimiento import *


app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indicador/nivelresponsabilidada/<name>', methods=['GET', 'POST'])
def Responsabilidad(name):
    session["responsabilidad"]=escape(name)
    contador=CantidadPorNivelResponsabilidad()
    return render_template('cantidadNivelResponsabilidad.html', contador = contador,dato=session["responsabilidad"])

@app.route('/indicador/institucion/<name>', methods=['GET', 'POST'])
def Institucion(name):
    session["institucion"]=escape(name)
    contador=CantidadPorInstitucion()
    return render_template('cantidadNivelResponsabilidad.html', contador = contador,dato=session["institucion"])


@app.route('/indicador/puesto/<name>', methods=['GET', 'POST'])
def Puesto(name):
    session["puesto"]=escape(name)
    contador=CantidadPorPuesto()
    return render_template('cantidadPuesto.html', contador = contador,dato=session["puesto"])


@app.route('/indicador/tipoarea/<name>', methods=['GET', 'POST'])
def TipoArea(name):
    session["tipoarea"]=escape(name)
    contador=CantidadPorTipoArea()
    return render_template('cantidadTipoArea.html', contador = contador,dato=session["tipoarea"])

@app.route('/indicador/tipoprocedimiento/<name>', methods=['GET', 'POST'])
def TipoProcedimiento(name):
    session["tipoprocedimiento"]=escape(name)
    contador=CantidadPorTipoProdedimiento()
    return render_template('cantidadTipoProcedimiento.html', contador = contador,dato=session["tipoprocedimiento"])


#1
@app.route('/indicador/procedimientotiempo/tiempo/<name>', methods=['GET', 'POST'])
def TipoProcedimientoAnios(name):
    session["tipoprocedimiento2"]=escape(name)
    datos=TipoProcedimientoPorTiempos()
    return render_template('tipoProdecimientoTiempo.html', datos = datos)



@app.route('/indicador/tipoarea/tiempo/<name>', methods=['GET', 'POST'])
def TipoAreaAnios(name):
    session["tipoarea2"]=escape(name)
    datos=TipoAreaTiempo()
    return render_template('tipoAreaTiempo.html', datos = datos)


@app.route('/indicador/nivelresponsabilidad/tiempo/<name>', methods=['GET', 'POST'])
def NivelResponsabilidadAnios(name):
    session["nivelresponsabilidad2"]=escape(name)
    datos=NivelResposabilidad()
    return render_template('nivelResponsabilidadTiempo.html', datos = datos)

@app.route('/indicador/InstitucionesPuesto/tiempo/<name>', methods=['GET', 'POST'])
def InstitucionesPuestoAnios(name):
    session["InstitucionesPuesto2"]=escape(name)
    datos=InstitucionesPuesto()
    return render_template('institucionesPuestosTiempo.html', datos = datos)

@app.route('/indicador/InstitucionesTiempo/tiempo/<name>', methods=['GET', 'POST'])
def InstitucionesTiempo(name):
    session["InstitucionesTiempo2"]=escape(name)
    datos=InstitucionesAnios()
    return render_template('InstitucionesTiempo.html', datos = datos)

#
#
#

@app.route('/indicador/clasificacion/tipoprocedimiento/mayor', methods=['GET', 'POST'])
def ClasificacionTPmayor():
    datos=TipoProcedimientoMayor()
    return render_template('ClasificacionTPmayor.html', datos = datos)


@app.route('/indicador/clasificacion/tipoprocedimiento/menor', methods=['GET', 'POST'])
def ClasificacionTPmenor():
    datos=TipoProcedimientoMenor()
    return render_template('ClasificacionTPmenor.html', datos = datos)

@app.route('/indicador/clasificacion/tipoarea/menor', methods=['GET', 'POST'])
def ClasificacionTAmenor():
    datos=TiposAreaMenor()
    return render_template('ClasificacionTAmenor.html', datos = datos)

@app.route('/indicador/clasificacion/tipoarea/mayor', methods=['GET', 'POST'])
def ClasificacionTAmayor():
    datos=TiposAreaMayor()
    return render_template('ClasificacionTAmayor.html', datos = datos)

@app.route('/indicador/clasificacion/puesto/mayor', methods=['GET', 'POST'])
def ClasificacionPUESTOmayor():
    datos=MujeresPuestoMayor()
    return render_template('ClasificacionPUESTOmayor.html', datos = datos)

@app.route('/indicador/clasificacion/puesto/menor', methods=['GET', 'POST'])
def ClasificacionPUESTOmenor():
    datos=MujeresPuestoMenor()
    return render_template('ClasificacionPUESTOmenor.html', datos = datos)

@app.route('/indicador/clasificacion/responsabilidad/menor', methods=['GET', 'POST'])
def ClasificacionResponsabilidadmenor():
    datos=ObtenerNivelesResponsabilidadMenor()
    return render_template('ClasificacionResponsabilidadmenor.html', datos = datos)

@app.route('/indicador/clasificacion/responsabilidad/mayor', methods=['GET', 'POST'])
def ClasificacionResponsabilidadmayor():
    datos=ObtenerNivelesResponsabilidadMayor()
    return render_template('ClasificacionResponsabilidadmayor.html', datos = datos)

@app.route('/indicador/clasificacion/institucion/mayor', methods=['GET', 'POST'])
def ClasificacionInstitucionmayor():
    datos=MujeresPorDependenciaMayor()
    return render_template('ClasificacionInstitucionmayor.html', datos = datos)

@app.route('/indicador/clasificacion/institucion/menor', methods=['GET', 'POST'])
def ClasificacionInstitucionmenor():
    datos=MujeresPorDependenciaMenor()
    return render_template('ClasificacionInstitucionmenor.html', datos = datos)


@app.route('/indicador/ver-instituciones', methods=['GET', 'POST'])
def VerInstituciones():
    datos=ObtenerDependencias()
    return render_template('VerInstituciones.html', datos = datos)


@app.route('/indicador/ver-niveles', methods=['GET', 'POST'])
def VerNivelesReponsabilidad():
    datos=ObtenerNivelesResponsabilidad()
    return render_template('VerNivelesReponsabilidad.html', datos = datos)


@app.route('/indicador/ver-puestos', methods=['GET', 'POST'])
def VerPuestos():
    datos=ObtenerPuestos()
    return render_template('VerPuestos.html', datos = datos)



@app.route('/indicador/ver-tipo-area', methods=['GET', 'POST'])
def VerTipoArea():
    datos=ObtenerTipoArea()
    return render_template('VerTipoArea.html', datos = datos)



@app.route('/indicador/ver-tipos-procedimiento', methods=['GET', 'POST'])
def VerProcedimientos():
    datos=TiposProcedimiento()
    return render_template('VerProcedimientos.html', datos = datos)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

# metodo en caso de errores
@app.errorhandler(404)
def page_not_found(e):
    return render_template('page-404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('page-500.html'), 500


@app.errorhandler(401)
def no_authorized(e):
    return render_template('page-500.html'), 401



if __name__ == '__main__':
    app.run(debug=True)