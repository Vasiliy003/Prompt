Vue.createApp({
    data() {
        return {
            message: 'Hello world!'
        }
    },
    methods: {
        setMessage(event) {
            this.message = event.target.value;
        }
    }
}).mount('#app')