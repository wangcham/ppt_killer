<template>
    <div>
        <el-collapse v-model="activename" accordion>
            <el-collapse-item title="基本用法">
                <h4 style="margin-bottom:5px;margin-top:0;font-family: 'Source Han Sans SC', sans-serif;">如果上面的蓝色方框一直显示正在加载，不要着急，耐心等待一会儿，请不要关闭网页。</h4>
                <h4 style="margin-top:1px;font-family: 'Source Han Sans SC', sans-serif;">AI生成回答之后，会弹出消息提示框，并且在蓝色方框下方生成MarkDown格式内容。</h4>
                <h4 style="margin-top:0;">有些时候由于服务器和网络的原因(或者上传的文件很大)，AI回复的速度会变得很慢，请保持耐心。</h4>
                <h3 style="margin-top:0;">MarkDown格式的效果类似这种的：</h3>
                <el-divider/>
                <h3 style="margin-top:0;">我很喜欢U2乐队,为什么呢？</h3>
                <ul style="margin-top:0;">
                    <li>因为他们的音乐很牛逼</li>
                    <li>因为我喜欢玩原神</li>
                    <li>因为我不是二次元</li>
                </ul>
                <el-divider/>
                <p style="margin-top:0;">以上就是得到的效果</p>
                <p style="margin-top:0;">如果你只有ppt文件，那么请使用外部网站或者Microsoft Powerpoint</p>
                <p style="margin-top:0;">将ppt文件转换成pptx文件，外部网站可以自己搜索去转换文件。</p>
                <h2>！本站不保存用户上传的任何文件！</h2>
            </el-collapse-item>
            <el-collapse-item title="不基本用法" name="2">
                <p>是这样的，在生成内容之后，可以选择保存AI生成的回复</p>
                <p>你可以选择输入的专属密钥（相当于令牌），密钥网站会替你保存，在你下次想要看自己生成的内容时，</p>
                <p>可以在上方输入你的密钥,这时，网站就可以检索出属于你的令牌的生成的内容</p>
                <p>不要担心是否会发生令牌重复的问题，网站会检查一切。</p>
                <h3>提示到这里就结束了，你很聪明，因为至少在使用前会去看看说明，感谢使用！</h3>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>

<script>
export default {
    name:'ClickTips',
    data(){
        return{
            activename:1,
        }
    }
}
</script>

<style>

</style>