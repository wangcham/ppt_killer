<template>
    <div>
    <el-divider />
    <h2>提示：</h2>
      <h4 style="margin-bottom:5px;margin-top:0;font-family: 'Source Han Sans SC', sans-serif;">如果上面的蓝色方框一直显示正在加载，不要着急，耐心等待一会儿，请不要关闭网页。</h4>
      <h4 style="margin-top:1px;font-family: 'Source Han Sans SC', sans-serif;">AI生成回答之后，会弹出消息提示框，并且在蓝色方框下方生成MarkDown格式内容。</h4>
      <h4 style="margin-top:0;">有些时候由于服务器和网络的原因，AI回复的速度会变得很慢，请保持耐心。</h4>
      <h3 style="margin-top:0;">MarkDown格式的效果类似这种的：</h3>
      <h3 style="margin-top:0;">我很喜欢U2乐队,为什么呢？</h3>
      <ul style="margin-top:0;">
        <li>因为他们的音乐很牛逼</li>
        <li>因为我喜欢玩原神</li>
        <li>因为我不是二次元</li>
      </ul>
      <p>这就是得到的效果，在得到AI回复后，本提示将会马上消失，祝你使用愉快!</p>
      <el-divider />
    </div>
</template>

<script>
export default {
    name:'LoadingTips',
}
</script>

<style>

</style>