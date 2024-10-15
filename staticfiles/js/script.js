const raw_statements = document.querySelector('.statements')
const readbtns = document.querySelectorAll('.read-btn')

const statements = JSON.parse(raw_statements.innerText)

const popup = document.querySelector('.popup')
const popupclose = document.querySelector('.popupclose')
const psidtxt = document.querySelector('.psidtxt')
const pstitle = document.querySelector('.pstitle')
const psdesc = document.querySelector('.psdesc')
const psdf = document.querySelector('.psdf')
const cardparent = document.querySelector('.cardparent')
const body = document.querySelector('.body')
console.log(statements)


const search = document.querySelector('.psidsearch')


readbtns.forEach(btn=>btn.addEventListener('click', popupFunction))

function popupFunction(e) {
    body.classList.toggle('active')
    let statement = statements.find(({pk})=>pk===parseInt(e.target.dataset.psid))
    console.log('sdfsdf', statement)
    popup.classList.toggle('active')

    psidtxt.innerText = "Problem Statement ID:   " + statement.pk
    pstitle.innerText = "Title:   " + statement.fields.title
    psdesc.innerText = "Description: " + statement.fields.description
    psdf.innerText ="Difficulty Level: " +statement.fields.difficulty
}
popupclose.addEventListener('click', ()=>{
    body.classList.toggle('active')
    popup.classList.toggle('active')
})

// search.addEventListener('input', (e)=>{
//     statements.forEach((result)=>{
//         cardparent.innerHTML = ''
//         let status = result.pk.toString().includes(e.target.value)
//         console.log(status)
//         if (status)
//         {
//             console.log("success")
//             cardparent.innerHTML += `<div class="w-full bg-[#F6F0E5] p-6 flex flex-col gap-1 rounded-md font-montserrat border shadow-sm hover:shadow-md cursor-pointer">
//             <div>
//                 <p class="text-xs opacity-50">Problem Statement ID: ${result.pk}</p>
//             </div>
//             <div class="mt-2">
//                 <p class="text-xl">${result.fields.title}</p>
//             </div>
//             <div class="flex gap-2 font-medium">
//                 <p class="text-xs opacity-50">Difficulty Level: ${result.fields.difficulty}</p>
//                 <span>|</span>
//                 <p class="text-xs opacity-50">Maximum ${result.fields.submissions} submission</p>
//             </div>
//             <div>
//                     <button class="border border-black py-1 px-4 rounded-md text-xs read-btn" data-psid="{{statement.id}}">
//                         Read more
//                     </button>
//             </div>
//         </div>`
//         }
      
//     })
// })