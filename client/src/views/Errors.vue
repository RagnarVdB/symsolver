<template>
  <div class="errors">
    <div id="variables">
      <h2>Number of Variables: </h2>
      <input
        v-model.number="varAmount"
        type="number"
        class="small"
        min="1"
        oninput="validity.valid||(value='')"
      >
    </div>
    <div id="func">
      <h2>function:</h2>
      <input
        v-model="func"
        type="text"
        class="large"
      >
    </div>
    <div id="values">
      <h2>Variables, values and errors</h2>
      <div id="values-table">
        <h3>Variable</h3>
        <h3>value</h3>
        <h3>error</h3>
        <input
          v-for="n in 3*varAmount"
          :key="n"
          type="text"
            
          @input="setvalues(n - 1, $event.target.value)"
        >
      </div>
      <p>
        Symbols in the func not entered as variables will be treated as parameters.
      </p>
    </div>
    <div id="preview">
      <p :key="latex">
        $${{ latex }}$$
      </p>
    </div>
    <p
      v-if="notAllVars && showErrors"
      class="error"
    >
      Please enter all variables.
    </p>
    <p
      v-if="invalidSymbolsfunc"
      class="error"
    >
      The func contains invalid symbols.
    </p>
    <p
      v-if="invalidSymbolsvalues"
      class="error"
    >
      One of the values contains invalid symbols.
    </p>
    <p
      v-if="notLowerAndUpper && showErrors"
      class="error"
    >
      All values should have both lower and upper values, or no values
    </p>
    <p
      v-if="error"
      class="error"
    >
      {{ errorMessage }}
    </p>
    <button
      id="Calculate"
      @click="calculate"
    >
      Calculate!
    </button>
    <div
      v-if="loading"
      class="lds-ring"
    >
      <div /><div /><div /><div />
    </div>
  </div>
</template>

<script>
import latexGenerator from '@/functions/latexGenerator.js'

export default {
  name: 'Integrals',
  data() {
    return {
      url: process.env.VUE_APP_IP + 'v1/errorprop', // environment variable, wijst naar localhost in development en server IP in productie
      varAmount: 1,
      func: '',
      values: [['', '', '']],
      showErrors: false,
      loading: false,
      error: false,
      errorMessage: ''
    }
  },
  computed: {
    latex() {
      let func
      try {
        func = latexGenerator(this.func)
      } catch (e) {
        func = 'invalid'
      }
      return func
    },
    invalidSymbolsfunc() {
      // true wanneer de func verkeerde symbolen bevat
      return false
    },
    invalidSymbolsvalues() {
      // true wanneer één van de grenzen verkeerde symbolen bevat
      return false
    },
    notAllVars() {
      // true wanneer niet alle vakjes voor variabelen correct zijn ingevuld
      return !this.values.every(bound => bound[0] && bound[0].match(/[a-z]/i)) || this.values.length != this.varAmount
    },
    notLowerAndUpper() {
      // true wanneer sommige grenzen enkel ondergrens of bovengrens hebben
      return !this.values.every(bound => (bound[1] && bound[2]) || !(bound[1] || bound[2]))
    }
  },
  watch: {
    latex() {
      // wacht tot volgende cycle event loop zodat nieuwe code gerenderd wordt
      this.$nextTick().then(() => { this.reRender() })
    }
  },
  mounted() {
    // laad mathjax
    let MathJax = document.createElement('script')
    MathJax.setAttribute('src', 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')
    document.head.appendChild(MathJax)
    this.reRender()
  },
  methods: {
    setvalues(n, value) {
      const row = Math.floor(n/3)
      const column = n % 3
      if (!this.values[row]) {
        this.values[row] = ['', '', ''] //voeg lege rij toe aan matrix voor nieuwe variabele
      }
      let new_row = this.values[row]
      new_row[column] = value
      this.$set(this.values, row, new_row) // gebruik $set voor reactiviteit
    },
    reRender() {
      if (window.MathJax) {
        window.MathJax.typeset()
      }
    },
    calculate() {
      this.$gtag.event('Errors', {
        'event_category': 'button',
        'event_label': 'errorcalc',
        'value': 'errorcalc'
      })
      this.showErrors = true
      if (!this.notAllVars && !this.invalidSymbolsfunc && !this.invalidSymbolsvalues && !this.notLowerAndUpper) {
        this.loading = true
        const body = JSON.stringify({
          func: this.func,
          values: this.values
        })
        console.log(this.url)
        console.log(body)
        fetch(this.url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          redirect: 'follow',
          body
        })
          .then(res => res.json())
          .then(data => {
            this.loading = false
            console.log(data)
            if (data.status !== 'error') {
              if (!data.message) {
                data.message = " "
              }
              this.$router.push({path: `/solution/${data.solution}/message/${data.message}`})
            } else {
              this.error = true
              this.errorMessage = data.message
            }
          })
          .catch(err => {
            console.error(err)
            this.loading = false
            this.error = true
            this.errorMessage = 'Something went wrong, the server or your internet connection may be down.'
            })
      }
    }
  }
}
</script>

<style scoped>
* {
  text-align: start;
}
h2 {
  color: #002F6C;
  font-size: 1.15rem;
  font-weight: 400;
}

h3 {
  font-weight: 300;
  font-size: 1rem;
}

p {
  font-size: 0.9rem;
  font-weight: 300;
  color: rgba(0, 0, 0, 0.6);
}

.errors {
  padding-bottom: 5vh;
}

button {
  grid-area: Button;
  margin-top: 40px;
  width: 50vw;
  height: 50px;
  background-color: #01579B;
  border: none;
  border-radius: 15px;
  color: white;
  align-self: center;
  text-align: center;
  font-size: 1.4rem;
  font-weight: 400;
}

input {
  border: none;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  border-radius: 7px;
  height: 40px;
  font-size: 1.2rem;
}

input.small {
  width: 60px;
  text-align: center;
}

input.large {
  width: 100%;
  height: 50px;
  padding-left: 13px;
  padding-right: 13px;
  border-radius: 12px;
  box-sizing: border-box;
  font-size: 1.1rem;
  color: #333333
}

.errors {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.errors > div > h2 {
  margin-bottom: 5px;
}

.errors div {
  margin-top: 20px;
}

#variables {
  margin-top: 70px;
  grid-area: Number;
  width: 100%;
  display: flex;
  align-items: center;
}

#variables h2{
  margin-right: 20px
}

#func {
  grid-area: func;
  display: flex;
  flex-direction: column;
}

#values {
  grid-area: values;
  display: flex;
  flex-direction: column;
  width: 100%;
}

#values-table {
  display: grid;
  width: 100%;
  grid-template-columns: 1fr 2fr 2fr;
  justify-items: center;
  gap: 20px 10px;
  margin-bottom: 20px;
}

#values p {
  margin-left: 8px;
}

#values-table input{
  width: 80%;
  text-align: center;
}

#preview {
  grid-area: Integral;
  margin-top: 40px;
  padding: 5px;
  width: 90%;
  height: fit-content;
  align-self: center;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  display: flex;
  justify-content: center;
  align-items: center;
  
}

#preview p {
  text-align: center;
  color: black;
  font-size: 1.3rem;
  overflow: auto;
  width: 100%;
}

.error {
  margin-top: 30px;
  color: red;
  font-size: 1rem;
}

.lds-ring {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
  align-self: center;
}
.lds-ring div {
  box-sizing: border-box;
  display: block;
  position: absolute;
  width: 64px;
  height: 64px;
  margin: 8px;
  border: 6px solid #01579B;
  border-radius: 50%;
  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  border-color: #01579B transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
  animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
  animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
  animation-delay: -0.15s;
}
@keyframes lds-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
/* Desktop versie */
@media screen and (min-width: 900px){
  .errors {
    justify-content: center;
    display: grid;
    margin-top: 80px;
    grid-template-columns: 400px 400px;
    grid-template-rows: auto;
    grid-gap: 3vh 8vw;
    grid-template-areas: 
    "Number Integral"
    "func Integral"
    "values Button";
    }
  #preview {
    margin-top: 0px;
  }
  #Calculate {
    grid-area: Button;
    width: 60%;
    justify-self: center;
  }
}


</style>
