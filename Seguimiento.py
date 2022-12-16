<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='styles.css') }}"
    />
    <title>Citas</title>
  </head>
  <body>
    <div class="box__home">
      <header class="header__home">
        <div class="wrap">
          <div class="headerBox">
            <div><p class="clinicName">Clinica Peralta</p></div>
            <div class="links">
              <a href="/">Agendar Cita</a><a href="/mostrarcitas">Ver Citas</a
              ><a href="#">Cancelar cita</a>
            </div>
          </div>
        </div>
      </header>
      <div class="wrap">
        <main class="mainTable">
          <div class="tableBox">
            <h1 class="formTitle">Todas las citas agendadas</h1>
            <div class="table">
              <h3 class="nombreHeader">Nombre</h3>
              <h3 class="apellidoHeader">Apellido</h3>
              <h3 class="cedulaHeader">Cedula</h3>
              <h3 class="telefonoHeader">Telefono</h3>
              <h3 class="fechaHeader">Fecha</h3>

              <div class="nombreColumn">
                {% for nombre in nombres %}
                <p>{{nombres[nombre]}}</p>
                {% endfor %}
              </div>
              <div class="apellidoColumn">
                {% for apellido in apellidos %}
                <p>{{apellidos[apellido]}}</p>
                {% endfor %}
              </div>

              <div class="cedulaColumn">
                {% for cedula in cedulas %}
                <p>{{cedulas[cedula]}}</p>
                {% endfor %}
              </div>

              <div class="telefonoColumn">
                {% for telefono in telefonos %}
                <p>{{telefonos[telefono]}}</p>
                {% endfor %}
              </div>

              <div class="fechaColumn">
                {% for fecha in fechas %}
                <p>{{fechas[fecha]}}</p>
                {% endfor %}
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </body>
</html>