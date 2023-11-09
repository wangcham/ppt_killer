import {createRouter,createWebHistory} from 'vue-router'
import GetSummarize from '../components/GetSummarize.vue'
import SearchOldData from '../components/SearchOldData.vue'
import DetailPage from '../components/DetailPage.vue'
import ShowOldData from '../components/ShowOldData.vue'
const routes = [
    { path :'/',redirect:'/GetSummarize'},
    { path :'/GetSummarize',name:'/GetSummarize',components:{GetSummarize:GetSummarize}},
    { path : '/SearchOldData',name:'/SearchOldData',components:{SearchOldData:SearchOldData}},
    { path : '/DetailPage',name:'/DetailPage',components:{DetailPage:DetailPage}},
    { path:'/ShowOldData',name:'/ShowOldData',components:{ShowOldData:ShowOldData}},
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router