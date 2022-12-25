const searchInput = document.getElementById('search-input')
const myGrid = document.getElementById('result-grid')
const loadingPlaceholder = document.getElementById('loading')
const noResPlaceholder = document.getElementById('no-results')

function search() {
  clearGrid(myGrid)
  clearGrid(noResPlaceholder)
  clearGrid(loadingPlaceholder)

  // fetch the search term from the search box
  const searchTerm = searchInput.value
  if (searchTerm === '') {
    return
  }

  loading()
  // fetch the search results from the server
  fetch('/search?query=' + searchTerm)
    .then(response => response.json())
    .then(data => {
      clearGrid(loadingPlaceholder)

      data.aziza.forEach(product => {
        injectNewProduct(product, 'aziza')
      })
      data.monoprix.forEach(product => {
        injectNewProduct(product, 'monoprix')
      })
      data.geant.forEach(product => {
        injectNewProduct(product, 'geant')
      })

      if (data.aziza.length === 0 && 
        data.monoprix.length === 0 &&
        data.geant.length === 0) {
        noRes()
      }
    })
    .catch(err => {
      console.log(err)
    })
}

function injectNewProduct(product, type) {
  const newProduct = document.createElement('div')
  newProduct.classList.add('product')
  newProduct.innerHTML = `
    <div>
    <a href="${product.link}" target="_blank"
        class="group h-60 block bg-white rounded-lg overflow-hidden shadow-lg relative mb-2 lg:mb-3">
        <img src="${product.image}"
            loading="lazy" alt="image"
            class="w-full h-full object-contain group-hover:scale-110 transition duration-200" />
    </a>

    <div class="flex justify-between items-start gap-2 px-2">
        <div class="flex flex-col">
            <a href="${product.link}" target="_blank"
                class="text-gray-800 hover:text-gray-500 text-lg lg:text-xl font-bold transition duration-100">${product.title}</a>
        </div>
    </div>

    <div class="flex justify-between items-start gap-2 px-2">
        <div class="flex flex-col">
            <img src="/static/images/${type}.png" alt="logo" class="w-20 h-12 object-contain" />
            <a href="${product.link}" target="_blank" class="text-gray-800 hover:text-gray-300 text-md font-bold transition duration-100">${product.price} DT</a>
        </div>
    </div>
</div>
    `
  myGrid.appendChild(newProduct)
}

function loading() {
  const loading = document.createElement('div')
  loading.classList.add('loading')
  loading.innerHTML = `<div class='flex items-center justify-center'>
  <div style="border-top-color:transparent" class="w-8 h-8 border-4 border-blue-200 rounded-full animate-spin"></div>
  <p class="ml-2">Chargement en cours...</p>
</div>`
  loadingPlaceholder.appendChild(loading)
}

function clearGrid(placeholder) {
  placeholder.innerHTML = ''
}

function noRes() {
  const noResElem = document.createElement('div')
  noResElem.classList.add('loading')
  noResElem.innerHTML = `<div class="w-full h-60 flex flex-col items-center justify-center">
  <div class="flex flex-col items-center justify-center">
      <img src="/static/images/no-results.png" alt="no results" class="h-40 object-contain" />
      <p class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-600 mt-2">Aucune donnée trouvée</p>
      <p class="md:text-lg xl:text-xl text-gray-500 mt-4">Veuillez réessayer avec un autre mot clé</p>
  </div>
</div>`
  noResPlaceholder.appendChild(noResElem)
}
