import * as THREE from 'three';
export function asteroidTrajectory(distance) {
    distance=Number(distance);
    if(isNaN(distance)) distance=2 ;
    distance*=5 ;
    const safe_distance=1.8 ;
    const flybyRadius=Math.max(distance , safe_distance);

    
    const start=new THREE.Vector3(THREE.MathUtils.randFloatSpread(12),
                THREE.MathUtils.randFloatSpread(12),THREE.MathUtils.randFloatSpread(-15));
    const angle = Math.random() * 2 * Math.PI ;            
    const  closestTOEarth= new THREE.Vector3(Math.cos(angle)*flybyRadius,
                           THREE.MathUtils.randFloatSpread(4),Math.sin(angle)*flybyRadius) ;
   
    if(closestTOEarth.length() < safe_distance) {
        closestTOEarth.setLength(safe_distance) ;
    }                       
    const end=closestTOEarth.clone().add(closestTOEarth.clone()).sub(start).normalize().multiplyScalar(8) ;    
    
    const curve = new THREE.QuadraticBezierCurve3(start,
         closestTOEarth , end) ;
    return curve ;
    
}
