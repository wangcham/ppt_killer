<template>
    <div class="footer">
        <el-link style="margin-right:30px;cursor: pointer;" @click="donateme = true" :underline='false' type="primary">
            Made By Wangcham
        </el-link>
        <el-link href="https://github.com/wangcham" type="success" target="_blank" :underline='false'>
        点击查看我的GitHub
            <el-icon style="margin-left:5px;margin-top: 2px;"><View /></el-icon>
        </el-link>
        <el-link @click="dialogvisible()" :underline='false' style="margin-left:30px;" type="primary">
            查看本站提示<el-icon style="margin-left:5px;margin-top: 1px;"><MagicStick /></el-icon>
        </el-link>
        <el-link style="margin-left:30px;" type="primary" :underline='false'>
            使用chatgpt<el-icon style="margin-left:5px;margin-top: 2px;"><Comment /></el-icon>
        </el-link>
        <!--tips-->
        <el-dialog v-model="showdialog">
            <ClickTips></ClickTips>
        </el-dialog>
        
        <el-dialog v-model="donateme" title="感谢捐赠捏~后续会支持更多功能的~">
            <DonateMe></DonateMe>
        </el-dialog>
    </div>
</template>

<script>
import DonateMe from './DonateMe.vue';
import ClickTips from './ClickTips.vue';
export default {
    name:'FooterTips',
    components:{
        ClickTips,
        DonateMe,
    },
    data(){
        return{
            showdialog:false,
            donateme:false
        }
    },
    methods:{
        dialogvisible(){
            this.showdialog = true;
        },
    }
}
</script>

<style>
.footer{
    display: flex;
    flex-direction: row;
    justify-content: center;
}
</style>