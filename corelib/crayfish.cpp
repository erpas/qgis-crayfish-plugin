/*
Crayfish - A collection of tools for TUFLOW and other hydraulic modelling packages
Copyright (C) 2015 Lutra Consulting

info at lutraconsulting dot co dot uk
Lutra Consulting
23 Chestnut Close
Burgess Hill
West Sussex
RH15 8HN

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
*/

#include "crayfish.h"

#include "crayfish_mesh_2dm.h"



Mesh* Crayfish::loadMesh(const QString& meshFile, LoadStatus* status)
{
  return loadMesh2DM(meshFile, status);
}

Mesh::DataSets Crayfish::loadDataSet(const QString& fileName, const Mesh* mesh, LoadStatus* status)
{
  if (status) status->clear();

  LoadStatus s;
  Mesh::DataSets lst;

  lst = loadBinaryDataSet(fileName, mesh, &s);
  if (status) *status = s;

  if (lst.count())
    return lst;

  // if the file format was not recognized, try to load it as ASCII dataset
  if (s.mLastError != LoadStatus::Err_UnknownFormat)
    return Mesh::DataSets();

  s.clear();

  lst = loadAsciiDataSet(fileName, mesh, &s);
  if (status) *status = s;

  if (lst.count())
    return lst;

  // if the file format was not recognized, try to load it as XMDF dataset
  if (s.mLastError != LoadStatus::Err_UnknownFormat)
    return Mesh::DataSets();

  s.clear();

  lst = loadXmdfDataSet(fileName, mesh, &s);
  if (status) *status = s;

  return lst;
}

