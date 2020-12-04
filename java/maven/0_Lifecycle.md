```
Clean Lifecycle在进行真正的构建之前进行一些清理工作。 
Default Lifecycle 构建的核心部分，编译，测试，打包，部署等等。 
Site Lifecycle 生成项目报告，站点，发布站点。 


生命周期(lifecycle)由多个阶段(phase)组成,这些阶段（phase）是有顺序的,后面的阶段依赖于前面的阶段.
每个阶段(phase)会挂接一到多个goal,
goal是maven里定义任务的最小单元。
我们和Maven最直接的交互方式就是调用这些生命周期阶段。
```
Clean Lifecycle
```
pre-clean
clean
post-clean
```
Default Lifecycle
```
validate
initialize
generate-sources
process-sources
generate-resources
process-resources
compile
process-classes
generate-test-sources
process-test-sources
generate-test-resources
process-test-resources
test-compile
process-test-classes
test
prepare-package
package
pre-integration-test
integration-test
post-integration-test
verify
install
deploy
```
Site Lifecycle 
```
pre-site
site
post-site
site-deploy
```

