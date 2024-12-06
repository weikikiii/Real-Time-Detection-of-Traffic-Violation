<?= $this->extend('template') ?>
<style>
    .button-container {
    display: flex;
    justify-content: center; /* 水平置中 */
    align-items: center;     /* 垂直置中 */
    flex-direction: row;     /* 按鈕水平排列 */
    text-align:center;
}
</style>

<?php
    $videoUrl = base_url($video_path);
?>

<?= $this->section('content') ?>
    <div class = run-container>
        <div id="videoContainer">
        <video width="640" height="360" controls>
            <source src="<?=  $videoUrl ?>" type="video/mp4">
        </video>
        </div>

        <!-- 我這邊是想要用submit啦 -->
        <form action="/RunController/run_program" method="POST" id="form">
            <input name = "video_path" value = "<?= $video_path?>" hidden>
            <input type="submit" name="click" value="執行程式" class="btn btn-secondary"/>
        </form>
        <div id="loadingMessage" style="display:none;">程式執行中，請稍後...</div>
        <div id="responseMessage"></div>
        <div id="result"></div>
    </div>
<?= $this->endSection() ?>
<!-- $('#loadingMessage').hide(); -->
<?= $this->section('script') ?>
    $(document).ready(function() {
        console.log("Hello World!");
        $('#form').on('submit', function(e) {
            e.preventDefault(); // 防止默认表单提交
            $('#loadingMessage').text("程式執行中，請稍後...");
            $('#loadingMessage').show();
            $.ajax({
                url: '<?= base_url('/RunController/run_program') ?>',
                method: 'POST',
                data: $(this).serialize(), // 序列化表单数据
                beforeSend: function() {
                    // 還沒回傳值之前
                    console.log("程式運行中...");
                },
                success: function(response) {
                    //$('#responseMessage').html(response); // 显示返回信息
                    var taskId = JSON.parse(response).taskId;
                    console.log(taskId);
                    if(taskId !== "not run"){
                        pollResult(taskId);
                    }
                    else{
                        $('#loadingMessage').text("程式已經執行過");
                    }
                    
                }
            });
        });
        function pollResult(taskId) {
            $.ajax({
                url: '<?= base_url('/RunController/check_result') ?>', // 查询结果的脚本
                type: 'GET',
                data: {
                    taskId: taskId // 发送任务ID
                },
                success: function(result) {
                    console.log(result);
                    
                    var jsonResult = JSON.parse(result);
                    if (jsonResult.status === 'not finished') {
                        // 如果未完成，继续轮询
                        setTimeout(function() { pollResult(taskId); }, 5000);   // 每5秒查詢一次
                    } else {
                        // 显示结果
                        //$('#result').text('程式輸出: ' + jsonResult.output);
                        $('#loadingMessage').text("程式執行完畢");
                        $.ajax({
                            url: '<?= base_url('/RunController/save_violating') ?>',
                            method: 'POST',
                            data: {output: jsonResult.output, video_path: $('input[name="video_path"]').val()},
                            success: function(response) {
                                //$('#responseMessage').html(response);
                            }
                        });
                    }
                },
                error: function(xhr, status, error) {
                    console.error('結果查詢失敗:', error);
                }
            });
        }
    });

<?= $this->endSection() ?>