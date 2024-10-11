const togglebtn = document.querySelector('.togglebtn')
const closebtn = document.querySelector('.closebtn')
const mobmenu = document.querySelector('.mobmenu')

const raw_statements = document.querySelector('.statements')
const readbtns = document.querySelectorAll('.read-btn')

const statements = JSON.parse(raw_statements.innerText)

const popup = document.querySelector('.popup')
const psidtxt = document.querySelector('.psidtxt')
const pstitle = document.querySelector('.pstitle')
const psdesc = document.querySelector('.psdesc')
const psdf = document.querySelector('.psdf')

togglebtn.addEventListener('click', ()=>{
    mobmenu.classList.toggle('active')
})
closebtn.addEventListener('click', ()=>{
    mobmenu.classList.toggle('active')
})

readbtns.forEach(btn=>btn.addEventListener('click', popupFunction))

function popupFunction(e) {
    let statement = statements.find(({pk})=>pk===parseInt(e.target.dataset.psid))
    console.log('sdfsdf', statement)
    popup.classList.toggle('active')

    psidtxt.innerText += statement.pk
    pstitle.innerText += statement.fields.title
    psdesc.innerText += statement.fields.description
    psdf.innerText += statement.fields.difficulty
    
}