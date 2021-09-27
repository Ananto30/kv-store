<script>
  import { fade } from "svelte/transition";
  import { page, service } from "./store.js";

  let fetching = false;

  $: serviceList = [];
  const fetchServices = () => {
    fetching = true;
    fetch("http://localhost:5000/api/services")
      .then((data) => data.json())
      .then((data) => {
        serviceList = data;
        fetching = false;
      });
  };

  function addServicePage() {
    $page = "addService";
  }

  function singleServicePage(serviceName) {
    $page = "singleService";
    $service = serviceName;
  }

  function deleteService(serviceName) {
    fetch("http://localhost:5000/api/services/" + serviceName, {
      method: "DELETE",
    })
      .then((response) => response.json())
      .then((data) => {
        fetchServices();
      });
  }

  fetchServices();
</script>

<div in:fade>
  <h2 class="ui header">Services</h2>
  <div class="ui relaxed divided list">
    {#if fetching}
      <div class="ui placeholder">
        <div class="line" />
        <div class="line" />
        <div class="line" />
      </div>
    {:else}
      {#each serviceList as service}
        <div class="item">
          <div class="right floated content">
            <button
              class="ui mini button"
              on:click={() => deleteService(service.service_name)}
            >
              Delete
            </button>
          </div>
          <i class="large middle aligned icon">⚙️</i>
          <div class="content">
            <!-- svelte-ignore a11y-missing-attribute -->
            <a
              class="header"
              on:click={() => singleServicePage(service.service_name)}
              >{service.service_name}</a
            >
            <div class="description">{service.key_count} key(s)</div>
          </div>
        </div>
      {/each}
    {/if}
  </div>
  <button
    class="ui right floated right labeled icon mini button"
    on:click={addServicePage}
  >
    <i class="right plus icon" />
    Add Service
  </button>
</div>
