function getLocation(){
    navigator.geolocation.getCurrentPosition();
}

function mostrarLatitud(posicion) {
    const lat = posicion.coords.latitude;
    return lat;
}

function mostrarLongitud(posicion){
    const lon = posicion.coords.longitude;
    return lon;
}

let appid = 'a463ce8116628bdeea5e2f598ece7127';
let lat = '-33.499940';
let lon = '-70.616395';
let lang = "sp";
let units = "metric";
let owmUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=${units}&lang=${lang}&appid=${appid}`;


$.getJSON(owmUrl, function(clima){
    let html =
        `<p>Pronóstico de hoy: <b>${clima.weather[0].description} </b></p>
        <p>La temperatura actual es <b>${clima.main.temp} °C </b></p>
        <p>Con una máxima de <b>${clima.main.temp_max} °C </b> </p>`;
    
    $('#clima').html(html);

    let img = `<img src="https://openweathermap.org/img/wn/${clima.weather[0].icon}.png" />`;

    $('#climg').html(img);
    
})


