function fechadehoy(){
    var fecha = new Date();
    var diaSemana = fecha.getDay();
    var dia = fecha.getDate();
    var mes = fecha.getMonth() + 1;
    var anio = fecha.getFullYear();

    var semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
    var diaHoy = semana[diaSemana - 1];

    var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    var mesActual = meses[mes - 1];

    let fechahoy = diaHoy + " " + dia + " de " + mesActual + " del " + anio;
    $("#fecha").html(fechahoy);
}


function relojdigital(){
    var tiempo = new Date();
    var minutos = tiempo.getMinutes();
    var segundos = tiempo.getSeconds();
    var hora = tiempo.getHours();
    
    var exthora;
    var horacompleta;

    if(minutos<10){
        minutos = "0" + minutos;
    }else{
        minutos = "" + minutos;
    }

    if(segundos<10){
        segundos = "0" + segundos;
    }
    else{
        segundos = "" + segundos;
    }

    if(hora >12){
        exthora = "PM";
    }
    else{
        exthora = "AM";
    }

    if(hora > 12){
        hora -=12;
    }
    else{
        hora = hora;
    }

    horacompleta = hora + ":" + minutos + ":" + segundos + " " + exthora;
    $("#reloj").html(horacompleta);
}

$(document).ready(function(){
    setInterval(relojdigital, 1000 );
    fechadehoy();
})