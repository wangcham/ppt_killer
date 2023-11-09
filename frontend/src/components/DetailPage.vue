<template>
  <div>
    <div v-html="compiledMarkdown">
      </div>
  </div>
</template>

<script>
import MarkdownIt from 'markdown-it';
import {store} from '../store/store.js'
export default {
    name:'DetailPage',
    data(){
        return{
            md:new MarkdownIt(),
            MarkDown:'',
            store,
        }
    },
    computed:{
        compiledMarkdown(){
            return this.md.render(this.MarkDown)
        },
    },
    mounted(){
        this.MarkDown = this.store.content
    },
}
</script>

<style>

</style>