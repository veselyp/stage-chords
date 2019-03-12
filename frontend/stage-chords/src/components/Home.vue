<template>
<div>
  <section class="hero is-light">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Stage chords</h2>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="card" v-for="survey in surveys" v-bind:key="survey.id">
        <div class="card-content">
          <p class="title">{{ survey.name}}</p>
          <p class='subtitle'>{{ survey.created_at.toDateString() }}</p>
        </div>
      </div>
    </div>
  </section>
</div>
</template>

<script>

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
