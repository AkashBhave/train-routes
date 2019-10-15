<template>
    <div id="app">
        <p>{{ data }}</p>
        <p>{{ errors }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            data: null,
            errors: []
        };
    },

    // Fetches posts when the component is created.
    created() {
        axios
            .get(
                `http://localhost:5000/solve?algorithm=a&city1=Leon&city2=Tucson`
            )
            .then(response => {
                this.data = response.data;
                console.log(response.data['distance']);
            })
            .catch(e => {
                this.errors.push(e);
            });
    }
};
</script>
