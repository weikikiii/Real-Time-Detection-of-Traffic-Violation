<?= $this->extend('template') ?>
<?= $this->section('content') ?>
    <style>
        .check-container {
            display: grid;
            text-align:center;
            justify-content: center; /* 垂直居中 */
        }
    </style>
    <div class = check-container>
        <form action="/CheckController/list" method="post">
            <input type="submit" value="將檔案寫入資料庫" class = "btn btn-secondary">
        </form>
        </br>
        <form action="/CheckController/is_run" method="post">
            <input type="submit" value="將影片變成沒有跑過" class = "btn btn-secondary">
        </form>

    </div>
<?= $this->endSection() ?>
