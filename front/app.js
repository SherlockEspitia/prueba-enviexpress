const URL = 'http://127.0.0.1:8000/items/'

let app = document.querySelector('#app')

let tabla = document.createElement('table')
let thead = document.createElement('thead')
let tr = document.createElement('tr')
let tbody = document.createElement('tbody')


let items = fetch(URL, {
    method:'GET',
    mode:'cors',
    headers:{
        'Access-Control-Allow-Origin':"*"
    }
}).then((res)=>{
    return res.json()
}).then(data=>{
    let cabeceras = []
    for(c of Object.keys(data[0])){
        cabeceras.push(c)       
    }
    cabeceras.forEach(c=>{
        const th = document.createElement('th');
        th.textContent = c
        tr.appendChild(th)
    })
    data.forEach(item=>{
        let trb = document.createElement('tr')

        for(const key in item){
            let tdb = document.createElement("td");
            tdb.textContent = item[key]
            trb.appendChild(tdb)            
        }
        tbody.appendChild(trb)
    })
})

thead.appendChild(tr)
tabla.appendChild(thead)
tabla.appendChild(tbody)
app.appendChild(tabla)
