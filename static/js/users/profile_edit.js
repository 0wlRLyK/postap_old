$(function () {

    /* SCRIPT TO OPEN THE MODAL WITH THE PREVIEW */
    $("#id_avatar").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#image").attr("src", e.target.result);
                $("#modalCrop").modal("show");
            }
            reader.readAsDataURL(this.files[0]);
        }
    });

    /* SCRIPTS TO HANDLE THE CROPPER BOX */
    var $image = $("#image");
    var cropBoxData;
    var canvasData;
    $("#modalCrop").on("shown.bs.modal", function () {
        $image.cropper({
            viewMode: 1,
            aspectRatio: 1,
            minCropBoxWidth: 100,
            minCropBoxHeight: 100,
            ready: function () {
                $image.cropper("setCanvasData", canvasData);
                $image.cropper("setCropBoxData", cropBoxData);
            }
        });
    }).on("hidden.bs.modal", function () {
        cropBoxData = $image.cropper("getCropBoxData");
        canvasData = $image.cropper("getCanvasData");
        $image.cropper("destroy");
    });

    $(".js-zoom-in").click(function () {
        $image.cropper("zoom", 0.1);
    });

    $(".js-zoom-out").click(function () {
        $image.cropper("zoom", -0.1);
    });

    /* SCRIPT TO COLLECT THE DATA AND POST TO THE SERVER */
    $(".js-crop-and-upload").click(function () {
        var cropData = $image.cropper("getData");
        console.log(cropData)
        $("#id_x").val(cropData["x"]);
        $("#id_y").val(cropData["y"]);
        $("#id_height").val(cropData["height"]);
        $("#id_width").val(cropData["width"]);
        $("#modalCrop").modal('hide');
    });
//    *********************
//     # SIGN IMAGE
//    *********************
    /* SCRIPT TO OPEN THE MODAL WITH THE PREVIEW */
    $("#id_sign_image").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#image_sign").attr("src", e.target.result);
                $("#modalCrop_sign").modal("show");
            }
            reader.readAsDataURL(this.files[0]);
        }
    });

    /* SCRIPTS TO HANDLE THE CROPPER BOX */
    var $image_sign = $("#image_sign");
    var cropBoxData;
    var canvasData;
    $("#modalCrop_sign").on("shown.bs.modal", function () {
        $image_sign.cropper({
            viewMode: 1,
            // aspectRatio: 1,
            minCropBoxWidth: 50,
            minCropBoxHeight: 50,
            ready: function () {
                $image_sign.cropper("setCanvasData", canvasData);
                $image_sign.cropper("setCropBoxData", cropBoxData);
            }
        });
    }).on("hidden.bs.modal", function () {
        cropBoxData = $image_sign.cropper("getCropBoxData");
        canvasData = $image_sign.cropper("getCanvasData");
        $image_sign.cropper("destroy");
    });

    $(".js-zoom-in_sign").click(function () {
        $image_sign.cropper("zoom", 0.1);
    });

    $(".js-zoom-out_sign").click(function () {
        $image_sign.cropper("zoom", -0.1);
    });

    /* SCRIPT TO COLLECT THE DATA AND POST TO THE SERVER */
    $(".js-crop-and-upload_sign").click(function () {
        var cropData_sign = $image_sign.cropper("getData");
        $("#id_x_sign").val(cropData_sign["x"]);
        $("#id_y_sign").val(cropData_sign["y"]);
        $("#id_height_sign").val(cropData_sign["height"]);
        $("#id_width_sign").val(cropData_sign["width"]);
        $("#modalCrop_sign").modal('hide');
    });

//    *********************
//     # BACKGROUND IMAGE
//    *********************
    /* SCRIPT TO OPEN THE MODAL WITH THE PREVIEW */
    $("#id_bg").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#image_bg").attr("src", e.target.result);
                $("#modalCrop_bg").modal("show");
            }
            reader.readAsDataURL(this.files[0]);
        }
    });

    /* SCRIPTS TO HANDLE THE CROPPER BOX */
    var $image_bg = $("#image_bg");
    var cropBoxData;
    var canvasData;

    $("#modalCrop_bg").on("shown.bs.modal", function () {
        $image_bg.croppie({
            enableExif: true,
            viewport: {
                width: 1920,
                height: 400,
                type: 'square'
            },
            boundary: {
                width: 1420,
                height: 400
            }
        });


    }).on("hidden.bs.modal", function () {
        cropBoxData = $image_bg.cropper("getCropBoxData");
        canvasData = $image_bg.cropper("getCanvasData");
        $image_bg.cropper("destroy");
    });


    /* SCRIPT TO COLLECT THE DATA AND POST TO THE SERVER */
    $(".js-crop-and-upload_bg").click(function () {
        var cropData_bg = $image_bg.croppie("get")["points"];
        // var crp = cropData_bg["points"]
        console.log(cropData_bg)
        $("#id_x_bg").val(cropData_bg[0]);
        $("#id_y_bg").val(cropData_bg[1]);
        $("#id_width_bg").val(cropData_bg[2]);
        $("#id_height_bg").val(cropData_bg[3]);
        $("#modalCrop_bg").modal('hide');
    });
});
