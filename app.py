
```python
import streamlit as st
import nibabel as nib
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="ToothFairy2 | Dental CBCT Analysis",
    layout="wide"
)

st.title("ToothFairy2 | Dental CBCT Analysis")
st.warning(
    "Research prototype — not validated for clinical decisions"
)

st.write(
    "Upload a dental CBCT segmentation mask in NIfTI format "
    "(.nii or .nii.gz) to explore 3D dental structures."
)

uploaded_file = st.file_uploader(
    "Upload segmentation mask",
    type=["nii", "gz"]
)

if uploaded_file is not None:
    try:
        image = nib.load(uploaded_file)
        mask = image.get_fdata()
        voxel_sizes = image.header.get_zooms()[:3]

        labels = np.unique(mask)
        labels = labels[labels != 0]

        if len(labels) == 0:
            st.info("No segmented structures were found.")
        else:
            selected_label = st.selectbox(
                "Select structure label",
                labels.tolist()
            )

            binary_mask = mask == selected_label
            voxel_volume = float(np.prod(voxel_sizes))
            volume_mm3 = float(binary_mask.sum() * voxel_volume)

            coords = np.argwhere(binary_mask)

            st.subheader("Quantitative report")
            st.metric("Volume (mm³)", f"{volume_mm3:.2f}")

            if len(coords) > 0:
                extents = (
                    coords.max(axis=0) - coords.min(axis=0) + 1
                ) * np.array(voxel_sizes)

                c1, c2, c3 = st.columns(3)
                c1.metric("Extent X (mm)", f"{extents[0]:.2f}")
                c2.metric("Extent Y (mm)", f"{extents[1]:.2f}")
                c3.metric("Extent Z (mm)", f"{extents[2]:.2f}")

                st.subheader("3D model")

                if len(coords) > 50000:
                    coords = coords[::max(1, len(coords) // 50000)]

                fig = go.Figure(
                    data=[
                        go.Scatter3d(
                            x=coords[:, 0] * voxel_sizes[0],
                            y=coords[:, 1] * voxel_sizes[1],
                            z=coords[:, 2] * voxel_sizes[2],
                            mode="markers",
                            marker=dict(size=2),
                            name=f"Label {selected_label}"
                        )
                    ]
                )

                fig.update_layout(
                    scene=dict(aspectmode="data"),
                    margin=dict(l=0, r=0, b=0, t=30)
                )

                st.plotly_chart(fig, use_container_width=True)

    except Exception as error:
        st.error(f"Could not read the uploaded file: {error}")
else:
    st.caption(
        "Supported input: a segmentation mask in NIfTI format."
    )
```
