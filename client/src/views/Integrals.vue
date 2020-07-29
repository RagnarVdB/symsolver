<template>
  <div class="integrals">
    <div id="variables">
      <h2>Number of Variables: </h2>
      <input type="number" v-model="varAmount" class="small_input">
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Integrals',
  data() {
    return {
      varAmount: 1,
      integrand: '',
      bounds: {},
    }
  }
}
</script>

<style scoped>
h2 {
  color: black;
  font-size: 1.3rem;
  font-weight: 400;
}

input {
  border: none;
  box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25);
  border-radius: 7px;
  height: 45px;
  font-size: 1.2rem;
}
.small_input {
  width: 70px;
  text-align: center;
}
.integrals {
  display: flex;
  padding: 20px;
}

.integrals div {
  margin-top: 20px;
}

#variables {
  width: 100%;
  display: flex;
  align-items: center;
  margin-top: 0px;
}

#variables h2{
  margin-right: 20px
}
</style>