<template>
  <div>
    <!-- slot for parent component to activate the file changer -->
    <div @click="launchFilePicker()">
      <slot name="activator"></slot>
    </div>
    <!-- image input: style is set to hidden and assigned a ref so that it can be triggered -->
    <input type="file"
       ref="file"
       :name="uploadFieldName"
       @change="onFileChange(
          $event.target.name, $event.target.files)"
       style="display:none">
    <!-- error dialog displays any potential error messages -->
    <b-modal hide-footer v-model="errorDialog" max-width="300">
        <b-card-text class="subheading">{{errorText}}</b-card-text>
          <b-button @click="errorDialog = false" class="btn btn-success float-right mt-1">Got it!</b-button>
    </b-modal>
  </div>
</template>

<script>
    export default {
      name: "imageLoader",
      data: ()=> ({
      errorDialog: null,
      errorText: '',
      uploadFieldName: 'file',
      maxSize: 1024
    }),
    props: {
    // Use "value" to enable using v-model
      loadEvent: String,
      value: Object,
    },
    methods: {
      launchFilePicker(){
        this.$refs.file.click();
      },
      onFileChange(fieldName, file) {
        const { maxSize } = this;
        let imageFile = file[0];

        if (file.length>0) {
          let size = imageFile.size / maxSize / maxSize;
          if (!imageFile.type.match('image.*')) {
            // check whether the upload is an image
            this.errorDialog = true;
            this.errorText = 'Please choose an image file';
            this.$emit('toggleLoadedNewImage', false)
          } else if (size>1) {
            // check whether the size is greater than the size limit
            this.errorDialog = true;
            this.errorText = 'Your file is too big! Please select an image under 1MB';
            this.$emit('toggleLoadedNewImage', false)
          } else {
            // Append file into FormData and turn file into image URL
            let formData = new FormData();
            let imageURL = URL.createObjectURL(imageFile);
            formData.append(fieldName, imageFile);
            // Emit the FormData and image URL to the parent component
            this.$emit('input', { formData, imageURL, imageFile });
            this.$emit(this.loadEvent, true);
          }
        }
      }
    }
    }
</script>

<style scoped>

</style>
