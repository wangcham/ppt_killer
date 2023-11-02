import {createRouter,createWebHistory} from 'vue-router'
import GetSummarize from '../components/GetSummarize.vue'
import SearchOldData from '../components/SearchOldData.vue'
const routes = [
    { path :'/',redirect:'/GetSummarize'},
    { path :'/GetSummarize',name:'/GetSummarize',components:{GetSummarize:GetSummarize}},
    { path : '/SearchOldData',name:'/SearchOldData',components:{SearchOldData:SearchOldData}},
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router