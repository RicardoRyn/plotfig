# fsLR

The midthickness, inflated, and very inflated surfaces are from the Conte69 atlas.
The sulcal depth maps were all generated from the 164k surface via:

```bash
wb_command -metric-resample ${sulc164k} ${164k_sphere} ${Xk_sphere} ADAP_BARY_AREAS ${sulc_Xk} \
           -area-metrics ${164k_vaavg} ${Xk_vaaavg}
```

Where `${Xk_sphere}` is the target sphere and `${164k_vaavg}` + `${Xk_vaavg}` are average vertex area maps.

基于HCP样本 `100206` 通过 HCP 处理流程生成的表面数据文件：

- `tpl-fsLR_den-32k_hemi-L_flat.surf.gii`
- `tpl-fsLR_den-32k_hemi-R_flat.surf.gii`
- `100206.L.sulc.32k_fs_LR.shape.gii`
- `100206.R.sulc.32k_fs_LR.shape.gii`
