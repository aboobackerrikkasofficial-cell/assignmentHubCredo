<template>
  <div class="page-container">
    <router-view/>
  </div>
</template>

<style>
html,body,#app{
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}
.page-container{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  min-height: 100vh;
  background-image:url('/src/assets/backgroundforassignment.jpg');
  background-size: cover;
  background-repeat:no-repeat;
}

/* Mobile Responsive */
@media (max-width: 600px) {
  .page-container {
    display: flex;
    justify-content: center;
    align-items: center;
    background-size: cover;
  }

  html, body, #app {
    height: auto;
    min-height: 100vh;
    overflow: hidden;
  }
}

</style>
